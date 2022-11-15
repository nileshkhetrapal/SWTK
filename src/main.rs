//Julien Marcuse's code
use std::{collections::HashMap, fs};
use serde::{Serialize, Deserialize};

//Frequency analysis on the number of tokens in every line
fn main() {
    let args: Vec<_> = std::env::args().skip(1).collect::<Vec<_>>();
    let file = args[0].clone();
    let contents = fs::read_to_string(file).unwrap();
    let mut tree = CharTree::new();
    let loaded = do_flag(&args, "-l", |path| {
        let contents = fs::read_to_string(path).unwrap();
        tree = CharTree::from_string(contents);
    });
    if !loaded {
        tree.train(contents.clone());
    }
    let mut saved = do_flag(&args, "-s", |path| {
       fs::write(path, tree.to_string()).unwrap();
    });
    if args.contains(&"-a".to_string()) {
        saved = true;
        contents.lines()
            .map(|line| tree.get_weirdness(&line))
            .map(|weirdness| average(&weirdness)).enumerate()
            .for_each(|(line, average)| println!("{}: {}", line + 1, average));
    }
    if !saved {
        println!("{:?}", tree.get_weirdness(&contents));
    }
}

fn average(nums: &Vec<u32>) -> f32 {
    nums.iter().sum::<u32>() as f32 / nums.len() as f32
}

fn do_flag(args: &Vec<String>, flag: &str, callback: impl FnOnce(&str) -> ()) -> bool {
    for i in 0..args.len() {
        if args[i] == flag {
            callback(&args[i + 1]);
            return true;
        }
    }
    false
}

#[derive(Serialize, Deserialize)]
struct CharTree {
    root: Node
}

#[derive(Serialize, Deserialize)]
struct Node {
    count: u32,
    children: HashMap<char, Node>,
}

impl CharTree {
    fn new() -> CharTree {
        CharTree {
            root: Node {
                count: 0,
                children: HashMap::new()
            }
        }
    }

    fn from_string(string: String) -> CharTree {
        serde_json::from_str(&string).unwrap()
    }

    fn train(&mut self, string: String) {
        let chars: Vec<char> = string.chars().collect();
        for i in 0..chars.len() {
            self.put(&chars[i..]);
        }
    }

    fn put(&mut self, key: &[char]) {
        Self::put_recur(&mut self.root, key);
    }

    fn put_recur(node: &mut Node, key: &[char]) {
        if key.is_empty() {
            return;
        }
        node.count += 1;
        let next = node.children.get_mut(&key[0]);
        match next {
            Some(n) => Self::put_recur(n, &key[1..]),
            _ => {
                node.children.insert(key[0], Node {
                    count: 0,
                    children: HashMap::new()
                });
            }
        }
    }

    fn depth(&self, key: &[char]) -> u32 {
        Self::depth_recur(&self.root, key)
    }

    fn depth_recur(node: &Node, key: &[char]) -> u32 {
        if key.len() == 0 {
            return 0;
        }
        match node.children.get(&key[0]) {
            Some(n) => Self::depth_recur(&n, &key[1..]) + 1,
            _ => 0
        }
    }

    fn get_weirdness(&self, string: &str) -> Vec<u32> {
        let mut weirdness = vec![];
        let chars: Vec<char> = string.chars().collect();
        for i in 0..chars.len() {
            weirdness.push(self.depth(&chars[i..]));
        }
        weirdness
    }
}

impl ToString for CharTree {
    fn to_string(&self) -> String {
        serde_json::to_string(&self).unwrap()
    }
}