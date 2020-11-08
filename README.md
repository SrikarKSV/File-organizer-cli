# File organizer CLI

Organize all the files in a folder into their respective category!

## Feature:

1. Multiple directories can be specified.
2. A single text file can be given containing all the directories to be sorted.
3. Sorted files can be logged into console.
4. Specific files can be excluded by providing their extensions!

---

### Usage:

- Copy the absolute path of the directory you want to organize.

```python
$ python main.py --directory "*absolute_path_of_directory*" "*absolute_path_of_second_directory*"
```

- To log the transfers

```python
$ python main.py --directory "*absolute_path_of_directory*" --log
```

- To exclude extensions

```python
$ python main.py --directory "*absolute_path_of_directory*" --exclude=.go,.css,.exe
```

- To provide a text file with the directories(Won't work if --directory is provided)

```python
$ python main.py --input *name_of_the_text_file.txt*
```

#### Shorthands for the flags

1. --directory : -d
2. --log : -l
3. --exclude : -e
4. --input : -i
