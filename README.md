# TanX.fi
Task Created You have been given a dataset of customer orders from an online store. Using Docker extract the data.
Orders Analysis
How to Run the Application
Build the Docker image:
docker build -t orders-analysis .
Run the Docker container:
docker run orders-analysis
How to Run the Tests
Build the Docker image for tests:
docker build -f Dockerfile.test -t orders-tests .
Run the Docker container for tests:
docker run orders-tests
Requirements
Docker
Python 3.11
pandas
pytest image PS E:\Tan> docker login Authenticating with existing credentials... Stored credentials invalid or expired Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one. You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/ Username (pravin2002): pravin2002 Password: Error response from daemon: Get "https://registry-1.docker.io/v2/": unauthorized: incorrect username or password PS E:\Tan> docker login Authenticating with existing credentials... Stored credentials invalid or expired Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one. You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/ Username (pravin2002): pravin2002 Password: Login Succeeded PS E:\Tan> docker build -t orders_analysis . [+] Building 38.3s (10/10) FINISHED docker:desktop-linux => [internal] load build definition from Dockerfile 0.0s => => transferring dockerfile: 434B 0.0s => [internal] load metadata for docker.io/library/python:3.11-slim 2.6s => [auth] library/python:pull token for registry-1.docker.io 0.0s => [internal] load .dockerignore 0.0s => => transferring context: 2B 0.0s => [1/4] FROM docker.io/library/python:3.11-slim@sha256:3f3c35617e79276c5f6a2e6a13cdbabdd10257332df963c90c986858b26fad5e 11.2s => => resolve docker.io/library/python:3.11-slim@sha256:3f3c35617e79276c5f6a2e6a13cdbabdd10257332df963c90c986858b26fad5e 0.0s => => sha256:3f3c35617e79276c5f6a2e6a13cdbabdd10257332df963c90c986858b26fad5e 9.12kB / 9.12kB 0.0s => => sha256:2bbbd2863f3a2cf5a60794c8cad4530d6be3c9e72f23730239146e61a345009f 1.94kB / 1.94kB 0.0s => => sha256:13d803497f988e563809a4c2664c4b9d23883a3a7ba3fbdad6d729dcaaf43e56 6.89kB / 6.89kB 0.0s => => sha256:efc2b5ad9eec05befa54239d53feeae3569ccbef689aa5e5dbfc25da6c4df559 29.13MB / 29.13MB 6.8s => => sha256:60462faabbc27679d4e1a907afda153c5f2294df5f752f0e706937779faa6d22 3.51MB / 3.51MB 1.1s => => sha256:11f0c4afa075fefa38e75f0bc033f3c60251827dfbecce64bf57bc67fc3718f0 12.87MB / 12.87MB 5.1s => => sha256:d8393bf961f1ad054e82d4740c6557c77315c37cb25c19036e329d6194617c13 230B / 230B 1.6s => => sha256:e1558965ee47a72ec3c70592a93ae13e931a2d0f5719ab6c643c4a531c103236 3.21MB / 3.21MB 7.1s => => extracting sha256:efc2b5ad9eec05befa54239d53feeae3569ccbef689aa5e5dbfc25da6c4df559 2.3s => => extracting sha256:60462faabbc27679d4e1a907afda153c5f2294df5f752f0e706937779faa6d22 0.2s => => extracting sha256:11f0c4afa075fefa38e75f0bc033f3c60251827dfbecce64bf57bc67fc3718f0 1.0s => => extracting sha256:d8393bf961f1ad054e82d4740c6557c77315c37cb25c19036e329d6194617c13 0.0s => => extracting sha256:e1558965ee47a72ec3c70592a93ae13e931a2d0f5719ab6c643c4a531c103236 0.4s => [internal] load build context 0.0s => => transferring context: 13.76kB 0.0s => [2/4] WORKDIR /app 0.2s => [3/4] COPY . /app 0.0s => [4/4] RUN pip install --no-cache-dir -r requirements.txt 23.2s => exporting to image 0.9s => => exporting layers 0.9s => => writing image sha256:49a3e10e63ef97ae8ce97166eb7695572142acfed0898c6c8df55345b14eb287 0.0s => => naming to docker.io/library/orders_analysis 0.0s View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/javpl18nvlebpuuxowjhond3n What's next: View a summary of image vulnerabilities and recommendations → docker scout quickview PS E:\Tan> docker run -it --name order_analysis_container order_analysis Unable to find image 'order_analysis:latest' locally docker: Error response from daemon: pull access denied for order_analysis, repository does not exist or may require 'docker login': denied: requested access to the resource is denied. See 'docker run --help'. PS E:\Tan> docker run order_analysis Unable to find image 'order_analysis:latest' locally docker: Error response from daemon: pull access denied for order_analysis, repository does not exist or may require 'docker login': denied: requested access to the resource is denied. See 'docker run --help'. PS E:\Tan> docker run -it --name orders_analysis_container orders_analysis Monthly Revenue: month total_revenue 0 2021-01 10.0 1 2021-02 60.0 2 2021-03 100.0 3 2021-04 50.0 Product Revenue: product_name total_revenue 0 Product A 60.0 1 Product B 40.0 2 Product C 30.0 3 Product D 40.0 4 Product E 50.0 Customer Revenue: customer_id total_revenue 0 1 60.0 1 2 80.0 2 3 80.0 Top Customers by Revenue: customer_id total_revenue 1 2 80.0 2 3 80.0 0 1 60.0 PS E:\Tan> docker images REPOSITORY TAG IMAGE ID CREATED SIZE orders_analysis latest 49a3e10e63ef 14 minutes ago 305MB PS E:\Tan> docker inspect orders_analysis [ { "Id": "sha256:49a3e10e63ef97ae8ce97166eb7695572142acfed0898c6c8df55345b14eb287", "RepoTags": [ "orders_analysis:latest" ], "RepoDigests": [], "Parent": "", "Comment": "buildkit.dockerfile.v0", "Created": "2024-07-27T16:54:22.515888985Z", "DockerVersion": "", "Author": "", "Config": { "Hostname": "", "Domainname": "", "User": "", "AttachStdin": false, "AttachStdout": false, "AttachStderr": false, "Tty": false, "OpenStdin": false, "StdinOnce": false, "Env": [ "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "LANG=C.UTF-8", "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D", "PYTHON_VERSION=3.11.9", "PYTHON_PIP_VERSION=24.0", "PYTHON_SETUPTOOLS_VERSION=65.5.1", "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/e03e1607ad60522cf34a92e834138eb89f57667c/public/get-pip.py", "PYTHON_GET_PIP_SHA256=ee09098395e42eb1f82ef4acb231a767a6ae85504a9cf9983223df0a7cbd35d7" ], "Cmd": [ "python", "order_analysis.py" ], "ArgsEscaped": true, "Image": "", "Volumes": null, "WorkingDir": "/app", "Entrypoint": null, "OnBuild": null, "Labels": null }, "Architecture": "amd64", "Os": "linux", "Size": 304884908, "GraphDriver": { "Data": { "LowerDir": "/var/lib/docker/overlay2/51mrr4exre19nm15exbc940yz/diff:/var/lib/docker/overlay2/6wdx9jxd2zx0g0eb83l2lncqi/diff:/var/lib/docker/overlay2/ddd9ad57899279c756e2bec5804269e86fbbe170e82121b08ae9a5cc9c5e8c0f/diff:/var/lib/docker/overlay2/2952a2c2a8bd8d7bab32626d5d64f88b7704abbf6b8ae4d2054375711acc8ef8/diff:/var/lib/docker/overlay2/a301df850c429dabe0e40bb0c5497efe396faf528c210484a5fd1d7527851d22/diff:/var/lib/docker/overlay2/0bbcffa3598c6ca585387c73957f1695961b42c1dd41478ee9bcedd76aaac0b7/diff:/var/lib/docker/overlay2/faf8c36780752384b8d20ac1e64769b73cf2e4b8b6e942daf7bf7f601af5c859/diff", "MergedDir": "/var/lib/docker/overlay2/5203etnnxvmsueaxisan9wsbr/merged", "UpperDir": "/var/lib/docker/overlay2/5203etnnxvmsueaxisan9wsbr/diff", "WorkDir": "/var/lib/docker/overlay2/5203etnnxvmsueaxisan9wsbr/work" }, "Name": "overlay2" }, "RootFS": { "Type": "layers", "Layers": [ "sha256:e0781bc8667fb5ebf954df4ae52997f6f5568ec9f07e21e5db7c9d324ed41e1f", "sha256:ed14f45b73f0b4cfaf33c9f4acadeb30a63a144e51aa73dc8ee588c8ec829524", "sha256:90be576ff39f484a6b8a0f5e019a1112148a27e4a6dfe2d3a290db26847da46c", "sha256:6dabc1b666f2b05528b89333ce3afda345a491c0e9afad6c0e3466847ea32efa", "sha256:081664a1d5748578861eb635b499d466a768e479a09af9f202ba1503af8d232c", "sha256:826b209d9a64aa4faf9297c08280e8cfb80641bf9060060c77237ef9bf96ceef", "sha256:58a529c5c8455e5d3215120c7b7cdcd7261fb2a2d0ba9d8a73a74ab131c91484", "sha256:ae8376049e89be0718a76b976f2d59af5c3f26c94e4cc6b394e7b18613885202" ] }, "Metadata": { "LastTagTime": "2024-07-27T16:54:23.398238789Z" } } ] PS E:\Tan> git init
Initialized empty Git repository in E:/Tan/.git/ PS E:\Tan> git add .

PS E:\Tan> git add .

PS E:\Tan> git commit -m "Initial commit"

[master (root-commit) 65afc59] Initial commit 6 files changed, 147 insertions(+) create mode 100644 .vscode/extensions.json create mode 100644 Dockerfile create mode 100644 pycache/test_orders.cpython-311-pytest-7.4.0.pyc create mode 100644 order_analysis.py create mode 100644 requirements.txt create mode 100644 test_orders.py PS E:\Tan> git remote add origin https://github.com/prav002/Docker_TanX.fi.git

PS E:\Tan> git add .

PS E:\Tan> git commit -m "Initial commit"

On branch master nothing to commit, working tree clean PS E:\Tan> git push -u origin master

info: please complete authentication in your browser... Enumerating objects: 10, done. Counting objects: 100% (10/10), done. Delta compression using up to 8 threads Compressing objects: 100% (8/8), done. Writing objects: 100% (10/10), 4.60 KiB | 941.00 KiB/s, done. Total 10 (delta 0), reused 0 (delta 0), pack-reused 0 remote: remote: Create a pull request for 'master' on GitHub by visiting: remote: https://github.com/prav002/Docker_TanX.fi/pull/new/master remote: To https://github.com/prav002/Docker_TanX.fi.git

[new branch] master -> master branch 'master' set up to track 'origin/master'. PS E:\Tan> image
Footer

About
Task Created You have been given a dataset of customer orders from an online store. Using Docker extract the data.

Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
Python
100.0%
Suggested workflows
Based on your tech stack
Python package logo
Python package
Create and test a Python package on multiple Python versions.
Django logo
Django
Build and Test a Django Project
SLSA Generic generator logo
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
More workflows
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
