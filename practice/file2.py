import file1

print('file __name__ = %s' % __name__)

if __name__ == '__main__':
    print('File 2 being run directly')
else:
    print('File 1 imported')