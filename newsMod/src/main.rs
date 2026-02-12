use reqwest::blocking::get;
use rss::Channel;
use std::io::BufReader;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let url = "https://www.spiegel.de/schlagzeilen/tops/index.rss";
    let response = get(url)?;
    let reader = BufReader::new(response);

    let channel = Channel::read_from(reader)?;

    if let Some(item) = channel.items().first() {
        let title = item.title().unwrap_or("Nothing..");

        println!(
            "{{\"text\":\"NEW: {}\", \"tooltip\":\"{}\"}}",
            title,
            item.link().unwrap_or("")
        );
    }
    Ok(())
}
