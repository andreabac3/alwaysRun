# alwaysRun
[![](https://img.shields.io/npm/l/unique-names-generator.svg)](https://github.com/andreasonny83/unique-names-generator/blob/master/LICENSE)

Python script for launch in daemon way, software that must always remain running, such as web servers.<br/>
AlwaysRun will take care of creating logs, handling the error and resuming the execution of your software.<br/>


## How to use:<br/>
Just use the following synopsis:      python3 alwaysRun.py yourCommandBash <br/>
You need to replace the keyword 'yourCommandBash' with for example "node server.js"<br/>

```sh
$ python3 alwaysRun.py node server.js
The current pid of subprocess: 9741
```

### Note:<br/>
## Use Case
You can use it in any Unix or Windows terminal<br/>
If your program has to end, that's not what you're looking for.<br/>

## Fix error
Exit Code (1): <br/>
If you find an exit code 1 it means that you have forgotten the argvs, read the paragraph "How to Use" to fix.</br>  

# Authors

* **Andrea Bacciu**  - [github](https://github.com/andreabac3)
 
