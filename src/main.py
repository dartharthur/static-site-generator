from textnode import TextNode, TextType

def main():
    valid_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(valid_node)

if __name__ == "__main__":
    main()
    
