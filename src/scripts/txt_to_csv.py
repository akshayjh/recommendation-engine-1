import os
import re
import io
import csv
import gzip

def convert_txt_to_csv(path_to_dir):
    for filename in os.listdir(path_to_dir):
        filename_without_ending = filename[:-4]
        with open(path_to_dir + filename, "r") as txt_file:
            string_buffer = io.StringIO()
            fieldnames = ["title", "raw_text", "html_stripped_text"]
            writer = csv.writer(string_buffer, delimiter="\t")
            writer.writerow(fieldnames)
           
            text_to_write = []
            lines = txt_file.read().splitlines()
            for i  in range(len(lines)):
                text_to_write.append(lines[i])
            remove_html_tags = re.compile("<.*?>")
            body_text_html_removed = re.sub(remove_html_tags, "", lines[1])
            text_to_write.append(body_text_html_removed)
            writer.writerow(text_to_write)
            with gzip.open("/home/mark/temp/jyllands-posten-csv/" + filename_without_ending + ".csv.gz", "w") as out_file:
                out_file.write(bytes(string_buffer.getvalue(), encoding="utf-8"))

if __name__ == "__main__":
    print("Starting conversion")
    convert_txt_to_csv("/home/mark/temp/jyllands-posten/")

    print("Done")
