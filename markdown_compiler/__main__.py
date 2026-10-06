#!/usr/bin/python3

'''Convert a Markdown document into an HTML file.'''

from markdown_compiler import convert_file


def main():
    # Process command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    # FIXME:
    # To get the command_lines test to pass,
    # You will need to uncomment the line below;
    # Then add the args.add_css variable as a parameter to convert_file
    parser.add_argument('--add_css', action='store_true')
    args = parser.parse_args()

    # Call the main function
    convert_file(args.input_file, args.add_css)


if __name__ == '__main__':
    main()
