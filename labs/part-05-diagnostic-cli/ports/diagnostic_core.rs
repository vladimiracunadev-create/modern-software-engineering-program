//! Puerto mínimo del contrato observable. Usa solo la biblioteca estándar.

use std::collections::HashMap;
use std::env;
use std::fs;

fn fail(message: &str) -> ! {
    eprintln!("{message}");
    std::process::exit(3);
}

fn main() {
    let path = env::args().nth(1).unwrap_or_else(|| fail("usage: diagnostic_core <contract-cases.tsv>"));
    let text = fs::read_to_string(path).unwrap_or_else(|error| fail(&format!("input: {error}")));
    for (index, line) in text.lines().enumerate() {
        if index == 0 || line.trim().is_empty() {
            continue;
        }
        let fields: Vec<&str> = line.split('|').collect();
        if fields.len() != 7 {
            fail(&format!("line {}: expected 7 fields", index + 1));
        }
        let budget: u32 = fields[1].parse().unwrap_or_else(|_| fail("budget must be u32"));
        let spent: u32 = fields[3].parse().unwrap_or_else(|_| fail("spent must be u32"));
        let cost: u32 = fields[4].parse().unwrap_or_else(|_| fail("test_cost must be u32"));
        if spent.checked_add(cost).map_or(true, |total| total > budget) {
            fail("budget_exceeded");
        }
        let outcomes: HashMap<&str, &str> = fields[5]
            .split(',')
            .map(|pair| pair.split_once('=').unwrap_or_else(|| fail("invalid outcome pair")))
            .collect();
        let remaining: Vec<&str> = fields[2]
            .split(',')
            .filter(|candidate| outcomes.get(candidate).copied() == Some(fields[6]))
            .collect();
        if remaining.is_empty() {
            fail("contradictory_observation");
        }
        println!("{}|ok|{}|{}", fields[0], remaining.join(","), spent + cost);
    }
}
