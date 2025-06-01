# DIRSNIFFER



`Dir Sniffer` is a simple Python script that checks whether certain directories are accessible on a given website. It scans a target URL using a wordlist of common directory names to identify potentially existing directories.

![enter image description here](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHV4aWhuZGgxZ2JjcW82aDB1ajFxa2liam00Y2RwYnJqb3BlaXFhMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2kXLNQypdX9O1A3zxX/giphy.gif)

### Features

-   Simple and fast directory scanning
    
-   Uses a wordlist for customizable scanning
    
-   HTTP status code checking
    
-   Easily modifiable
    

### Usage

    python dirsniffer.py -u https://example-site.com -w wordlist.txt -t 1

-   `-u`: Target URL
    
-   `-w`: Wordlist file containing directory names
-   `-t`: Search per Second
    

### Purpose

This tool is developed for educational and security testing purposes. Use only on systems you have explicit permission to test.
