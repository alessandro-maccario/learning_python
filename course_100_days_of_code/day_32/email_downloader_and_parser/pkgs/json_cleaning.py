import re
import os
import sys
import json

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import INFO_TO_BE_REMOVED_FROM_JSON


class JSONCleaner:
    def __init__(self) -> None:
        pass

    def json_cleaning(
        self, read_file_path: os.PathLike, saving_file_path: os.PathLike
    ) -> None:
        """Cleans the JSON file to extract only relevant hyperlinks in the specified format.


        Parameters
        ----------
        file_path : os.PathLike
            Define the file path for the JSON file
        """
        links = []
        # If the file exists, load its current content
        if os.path.isfile(read_file_path):
            with open(read_file_path, "r") as file:
                # Load existing data
                data = json.load(file)

                # Pattern to match [Text](URL)
                pattern = r"\[(.*?)\]\((.*?)\)"
                for msg in data:
                    message_content = msg["message"][0].replace("\n", "")
                    matches = re.findall(pattern, message_content)

                    for text, url in matches:
                        # do not consider the [Text](URL) if contains specific words, just noise
                        if text in INFO_TO_BE_REMOVED_FROM_JSON or "premium" in url:
                            continue
                        # print(f"Found link: {text} - {url}\n")
                        links.append({"text": text, "url": url})

            # remove any duplicates
            self.save_to_json(links=links, output_path=saving_file_path)

    def save_to_json(self, links: list, output_path: os.PathLike):
        """Dump the links list to a JSON file.

        Parameters
        ----------
        links : list
            List containing the links to be saved to JSON
        output_path : os.PathLike
            Output the JSON file contains only the relevant links
        """
        # Save extracted links to new JSON
        with open(output_path, "w", encoding="latin1") as output_file:
            json.dump(
                links,
                output_file,
                ensure_ascii=False,
                indent=4,
            )
