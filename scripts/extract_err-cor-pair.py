# coding: utf-8

import argparse
import codecs
import json
import re
import platform

language = ['Korean', 'English', 'Japanese', 'Mandarin', 'Traditional Chinese',
            'Vietnamese', 'German', 'French', 'Other language', 'Spanish',
            'Indonesian', 'Russian', 'Arabic', 'Thai', 'Swedish', 'Dutch',
            'Hebrew', 'Tagalog', 'Portuguese(Brazil)', 'Cantonese', 'Italian',
            'Esperanto', 'Hawaiian', 'Afrikaans', 'Mongolian', 'Hindi', 'Polish',
            'Finnish', 'Greek', 'Bihari', 'Farsi', 'Urdu', 'Turkish', 'Portuguese(Portugal)',
            'Bulgarian', 'Norwegian', 'Romanian', 'Albanian', 'Ukrainian', 'Catalan',
            'Latvian', 'Danish', 'Serbian', 'Slovak', 'Georgian', 'Hungarian', 'Malaysian',
            'Icelandic', 'Latin', 'Laotian', 'Croatian', 'Lithuanian', 'Bengali', 'Tongan',
            'Slovenian', 'Swahili', 'Irish', 'Czech', 'Estonian', 'Khmer', 'Javanese', 'Sinhalese',
            'Sanskrit', 'Armenian', 'Tamil', 'Basque', 'Welsh', 'Bosnian', 'Macedonian', 'Telugu',
            'Uzbek', 'Gaelic', 'Azerbaijanian', 'Tibetan', 'Panjabi', 'Marathi', 'Yiddish', 'Ainu',
            'Haitian', 'Slavic']
color_tags = ["f-red", "f-blue", "f-bold"]
sline_tag = "sline]"


def main():
    assert platform.python_version_tuple()[0] == '3', 'This program supports only python3'
    args = parse_args()
    data_num = 0
    error_num = 0
    with codecs.open(args.data_path, 'r', encoding='utf8') as f:
        for line in f:
            data_num += 1
            try:
                jsonData = json.loads(line, strict=False)
                l2_langs, l1_lang = jsonData[2], jsonData[3]
                orig_sents, corr_sents = jsonData[4], jsonData[5]
                if (args.l1 == None or args.l1 == l1_lang) and args.l2 in l2_langs:
                    outputs = make_sent_pair(orig_sents, corr_sents, args)
                    for output in outputs:
                        print(output)
            except:
                error_num += 1
                pass

def make_sent_pair(orig_sents, corr_sents, args):
    outputs = []
    for i, orig_sent in enumerate(orig_sents):
        orig_sent = orig_sent.replace('\t', ' ')
        if len(corr_sents[i]) > 0:
            tag_err = False
            for corr_sent in corr_sents[i]:
                corr_sent = corr_sent.replace('\t', ' ')
                text, tag_err = delete_tags_color(corr_sent, tag_err, args)
                if sline_tag in text:
                    text, tag_err = delete_tags_sline(text, tag_err, args)
                if not tag_err and text != "":
                    output = orig_sent + "\t" + text
                    outputs.append(output)
        else:
            output = orig_sent + "\t" + orig_sent
            outputs.append(output)

    return outputs

def delete_tags_sline(text, tag_err, args):
    s_sline = "[sline]"
    e_sline = "[/sline]"
    if args.tags:
        return text
    words = text.split(" ")
    total_s = total_e = 0
    output_lists, tmp_list = [], []
    for word in words:
        num_s = word.count(s_sline)
        num_e = word.count(e_sline)

        total_s += num_s
        total_e += num_e
        tmp_list.append(word)
        if total_s == 0 and total_e == 0:
            output_lists.append(word)
            tmp_list = []
        elif total_s == total_e:
            tmp_text = " ".join(tmp_list)
            tmp_text = re.sub(r"\[sline\](.*)\[\/sline\]", r"", tmp_text)
            if tmp_text != "":
                output_lists.append(tmp_text)
            total_s = total_e = 0
            tmp_list = []
    text = " ".join(output_lists)

    if sline_tag in text:
        tag_err = True

    text = re.sub(r'\s+', ' ', text)
    return text, tag_err

def delete_tags_color(text, tag_err, args):
    if args.tags:
        return text
    text = replace_tags(text)

    if text == None:
        text = ""
    for tag in color_tags:
        s = "\[" + tag + "\]"
        e = "\[\/" + tag + "\]"
        text = re.sub(r"%s" % s, r"", text)
        text = re.sub(r"%s" % e, r"", text)
        if tag in text:
            tag_err = True

    return text, tag_err

def replace_tags(s):
    s = s.replace("[赤]", "[f-red]")
    s = s.replace("[/赤]", "[/f-red]")
    s = s.replace("[青]", "[f-blue]")
    s = s.replace("[/青]", "[/f-blue]")
    return s

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", dest="data_path", type=str, metavar='<str>', required=True, help="The path to the data set")
    parser.add_argument("-l2", "--learn-lang", dest="l2", type=str, metavar='<str>', required=False, default='English', help="L2 language")
    parser.add_argument("-l1", "--native-lang", dest="l1", type=str, metavar='<str>', required=False, default=None, help="L1 language")
    parser.add_argument("-tags", "--remain-tags", dest="tags", default=False, action='store_true', help="If you want to remain tags (e.g. [f-red]), please use this option")

    args = parser.parse_args()

    assert args.l2 in language
    if args.l1 != None:
        assert args.l1 in language

    return args


if __name__ == "__main__":
    main()