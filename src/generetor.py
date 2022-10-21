import csv
import os
import copy

abbr = {'Graph Matching': 'GM', 'Travelling Salesman Problem': 'TSP', 'Vehicle Routing Problem': 'VRP',
        'Job Shop Scheduling Problem': 'JSSP', 'Bin Packing Problem': 'BPP', 'Graph Edit Distance': 'GED',
        'Maximal Common Subgraph': 'MCS', 'Maximal Independent Set': 'MIS', 'Boolean Satisfiability': 'SAT',
        'Quadratic Assignment Problem': 'QAP',
        'Hamiltonian Cycle Problem': 'HCP',
        'Multiple Travelling Salesman Problem': 'mTSP',
        'Electronic Design Automation': 'EDA',
        'Orienteering Problem': 'OP'}


def sort_by_time(elem):
    return elem[3]

def write_category(file, content, n, index, href):
    num = 0
    for name in content.keys():
        num += 1
        if name == 'paper':
            num -= 1
            continue
        file.writelines('<tr>\n')
        name_index = name.replace(" ", "-").replace("/","").lower()
        if name in abbr:
            file.writelines('\t<td>'+'&emsp;'*n+'<a href=#{}>'.format(href+name_index)+ index + str(num) 
                            +' {} ({})</a></td>\n'.format(name, abbr[name]))
        else:
            file.writelines('\t<td>'+'&emsp;'*n+'<a href=#{}>'.format(href+name_index)+ index + str(num)
                            +' {}</a></td>\n'.format(name))
        file.writelines('</tr>\n')
        write_category(file, content[name], n+1, index+str(num)+'.', href+name_index)

def write_content(file, content, path):
    for name in content.keys():
        if name == 'paper':
            file.writelines("### [{}](#content)".format(path))
            file.write('\n')
            file.write('\n')
            num = 0
            for paper in content[name]:
                paper = [p.strip() for p in paper]
                num += 1
                # "category", "title", "publisher", "year", "type", "link", "authors, *code"
                if paper[7] == "":
                    file.writelines(
                        "{}. **{}** {}, {}. [{}]({})".format(num, paper[1], paper[2], paper[3], paper[4], paper[5]))
                else:
                    file.writelines(
                        "{}. **{}** {}, {}. [{}]({}), [code]({})".format(num, paper[1], paper[2], paper[3], paper[4],
                                                                        paper[5], paper[7]))
                file.write('\n')
                file.write('\n')
                file.writelines("    *{}*".format(paper[6]))
                file.write('\n')
                file.write('\n')
            continue
        path1 = path + name
        write_content(file, content[name], path1+'/')


def csv2md(csvFile, mdFile, header):
    csvFile = open(csvFile, "r", encoding='utf-8')
    reader = csv.reader(csvFile)
    raw_papers = []
    papers = []
    for item in reader:
        if reader.line_num == 1:
            continue
        raw_papers.append(item)
    csvFile.close()

    classes = []
    for paper in raw_papers:
        if ";" in paper[0]:
            paper_classes = paper[0].split(";")
            paper_classes = [cls.strip() for cls in paper_classes]
        else:
            paper_classes = [paper[0].strip()]
        for cls in paper_classes:
            if cls not in classes:
                classes.append(cls)

    content = {}
    for c in classes:
        path = c.split('//')
        if path[0] not in content.keys():
            content[path[0]] = {}
        pa_1 = content[path[0]]
        for pa in path[1:]:
            if pa not in pa_1.keys():
                pa_1[pa] = {}
            pa_1 = pa_1[pa]

    for c in classes:
        p = []
        for paper in raw_papers:
            if c in paper[0]:
                new_paper = copy.deepcopy(paper)
                new_paper[0] = c
                p.append(new_paper)
        p.sort(key=sort_by_time)
        path = c.split('//')
        pa_1 = content[path[0]]
        for pa in path[1:]:
            pa_1 = pa_1[pa]
        pa_1['paper'] = p


    command = "cp " + header + " " + mdFile
    os.system(command)
    with open(mdFile, "a", encoding='utf-8') as file:
        # write category
        write_category(file, content, 0, '', '')
        file.writelines('</table>\n')

        # write content
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')

        write_content(file, content, '')


if __name__ == '__main__':
    # md2csv("../README.md", "../data/papers.csv")
    csv2md("../data/papers.csv", "../README.md", "../data/header.md")