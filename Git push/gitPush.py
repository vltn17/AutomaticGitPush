import os, sys;
from github import Github;

def getGithubLogin(arguments):
    try:
        file = open(arguments[0][:-len("Git push/gitPush.py")] + "githubLogin.txt", "r");
        fileData = file.readlines();

        return fileData;
    except:
        print('!!! You miss to set your github login data.');
        print('Call gitPush --setLoginInfos to fix this error');
        print('See "gitPush --help" for more infos.');
        print();

        return "False";



def gitCommit(arguments):
    path = arguments[1];

    try:
        commitName = arguments[2];
    except:
        print('You miss to write the commit description.');
        return False;

    email = getGithubLogin(arguments)[0][:-len("\n")];
    mdp = getGithubLogin(arguments)[1][:-len("\n")];

    if email == "False" or mdp == "False":
        return False;

    print('Going to ' + path);
    os.chdir(path);

    print();

    print('Configurating user identification to github for the project.');
    os.system('git config user.email "' + email + '"');

    print();

    print('Do commit');
    os.system('git add .');
    os.system('git commit -m "' + commitName + '"');
    os.system('git push -u origin master');



def setLoginInfos():
    print("What is your github account email adress ?");
    email = input();

    print();

    print("What is your github account password ?");
    password = input();

    file = open(arguments[0][:-len("Git push/gitPush.py")] + "githubLogin.txt","a+");
    file.write(email + "\n");
    file.write(password + "\n");
    file.close();



def help(): # function help that list all function and there utilisation
    print();

    print('How to use git push:');
    print("    _ gitPush <commit description>");
    print("    _ gitPush --setLoginInfos");
    print("    _ gitPush --help");

    print();

    print('gitPush <commit description>:');
    print('    your commit description need to be between quotation mark.');

    print();
    
    print('!!! *** !!!');
    print();
    print('Important: before using gitPush you NEED:');
    print('    to refers your github account email adress and github password');
    print();
    print('!!! *** !!!');



def main():
    arguments = sys.argv;

    if "--help" in arguments: # run the help function
        help();
    elif "--setLoginInfos" in arguments: # run setLoginInfos function
        setLoginInfos();
    else: # create the project
        gitCommit(arguments);

main();