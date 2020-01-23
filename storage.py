import json, os, tempfile, argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('-key', '--key', dest='key_name')
parser.add_argument('-val', '--val', dest='value')
args = parser.parse_args()

def read_storage(file_name):
    with open(file_name) as f:
        return json.load(f)

def save_storage(storage, file_name):
    with open(file_name, 'w') as f:
        json.dump(storage, f)

if __name__ == '__main__':
    storage = defaultdict(list)
    storage_file_name = os.path.join(tempfile.gettempdir(), 'storage.data')
    key = args.key_name
    val = args.value

    if not os.path.exists(storage_file_name):
        if key and val:
            storage[key].append(val)
            print(val)
            save_storage(storage, storage_file_name)
    else:
        raw_storage = read_storage(storage_file_name)
        for k, v in raw_storage.items():
            storage[k].extend(v)
        if key:
            if val:
                storage[key].append(val)
                print('key11', key)
                print('val11', val)
                save_storage(storage, storage_file_name)
            else:
                print(list(storage[key]))
        else:
                print(None)




