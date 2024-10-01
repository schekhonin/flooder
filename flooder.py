#!/usr/bin/python3
import os

def get_free_space(path):
    statvfs = os.statvfs(path)
    return statvfs.f_bavail * statvfs.f_frsize

def fill_space():
    file_path = '/media/root/Part1/filler'
    mount_point = '/media/root/Part1'


    try:
        with open(file_path, 'wb') as f:
            print(f'Filling space {file_path}')
            while True:
                free_space = get_free_space(mount_point)
                print(f'Free space left: {free_space // (1024 * 1024)}MB')
                f.write(b'\x00'*1024 * 1024 * 100)
                f.flush
            f.close()
    except OSError as e:
        print(f'Error occured: {e}')
    finally:
        print('done')

if __name__ == "__main__":
    fill_space()
