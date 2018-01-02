## git tutorial


### download

[download git](https://git-scm.com/downloads)

### 打开git bash

windows下在某个文件夹下右键鼠标打开git bash

### git clone

第一次下载github上某个repository的代码，在git bash里输入

```
$ git clone https://github.com/ashengtx/python-tutorial.git
```

### git pull

如果已经下载过，需要更新，则在项目根目录使用git pull更新代码

```
~/python-tutorial$ git pull
```

如果有修改过一些文件，可能发生冲突，把冲突的文件删除即可

### git status

查看代码的变化

```
~/python-tutorial$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    git.md


```

### git add .

将所有代码变化加入缓冲区

```
~/python-tutorial$ git add .
```

### git commit

将缓冲区的代码变化commit到本地仓库

```
~/python-tutorial$ git commit -m "update git.md"
```

### git push

将本地仓库的commit推到github

```
~/python-tutorial$ git push origin master
```
