<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Making_a_service" />

  &#xa0;

  <!-- <a href="https://making_a_service.netlify.app">Demo</a> -->
</div>

<h1 align="center">Migrathor: Migrating everything on your openstack except your instances</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/making_a_service?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Making_a_service 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/vishwamithra37" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This project is used to export, backup, and import OpenStack user data without touching the backend. <br>
This is done with the help of admin rc file and openstackclient. The source deployment structure is first <br> read with the help of 'list' commands and are stored in json format in the temp folder. 
<br> This is done with the help of '  migrathor.sh '.

<br>
<br>
After that, it is important to have a clean destiantion openstack; so that the import of the source openstack won't be messing up the existing users. However, it is required to mention that:
<ul>
<li>The destination requires a public1 (Can be changed when needed) network as external network.</li>
<li>The services project will not be touched. But source users maybe created.</li>
<li>Make sure to have the required resources to transfer the source deployment.</li>
<li>Security groups are not yet covered!!</li>
</ul>

Also, some stream lining needs to be done. 

To backup/export:
```
bash migrathor.sh source_admin.rc
```
To import:
```
bash migrain2 destination_admin.rc
```



## :sparkles: Features ##

:heavy_check_mark: Backup your openstack and store the required files in one temp folder!<br> 
:heavy_check_mark: Deployment agnostic, you only need admin rights of the openstack and the RC file!<br>
:heavy_check_mark: Easy to tead, modify and edit to match your needs!

## :rocket: Technologies ##

The following tools were used in this project:

- [shell](https://www.tutorialspoint.com/unix/unix-what-is-shell.html)
- [python](https://www.python.org/)
- [opestackclient](https://pypi.org/project/python-openstackclient/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [pip](https://pypi.org/project/pip/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/vishwamithra37/Migrathor

# Access
$ cd Migrathor

# Install dependencies
$ pip install openstackclient

# Run the project
$ bash migrathor.sh source_admin.rc

# The script will start pulling stuff out of the openstack deployment and store in temp folder.
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/vishwamithra37" target="_blank">Vishwa Mithra</a>

&#xa0;

<a href="#top">Back to top</a>
