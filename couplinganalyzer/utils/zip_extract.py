import zipfile
from code_extract import parse_code
from depgraph import DepGraph

def get_code_from_zip(filename):
    '''fetches the java code from a file with the given filename'''

    if filename[-4:] != '.zip':
        raise Exception('File is not a ZIP file.')

    zip_file = zipfile.ZipFile(filename)

    code_txt = []

    for zip_member in zip_file.infolist():
        # read in all the java code in the zip file
        # skip anything that does not have a .java file extension
        member_filename = zip_member.filename
        extension = member_filename[-5:]
        if extension == '.java':
            code_txt.append(zip_file.read(member_filename))

    zip_file.close()

    return code_txt

def process_zip(filename):
    '''processes the zip_file and generates the dependency graph'''
    code_list = get_code_from_zip(filename)
    type_decls = parse_code(code_list)
    graph = DepGraph(type_decls)

    results = graph.get_all_coupling()

    sorted_results = sorted(zip(results.keys(), results.values()),
                            key=lambda x: x[1])

    return graph, sorted_results
