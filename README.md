
### Step-by-Step Procedure to Push to GitHub from PyCharm

1. **Open Project in PyCharm**:
   - Open your Radahn project in PyCharm.

2. **Initialize Git Repository**:
   - Go to `VCS` > `Enable Version Control Integration`.
   - Choose `Git` from the dropdown and click `OK`.

3. **Add Files to Git**:
   - Right-click on the project folder and select `Git` > `Add`.

4. **Commit Changes**:
   - Go to `VCS` > `Commit`.
   - Select all the files you want to commit, add a commit message, and click `Commit`.

5. **Push to GitHub**:
   - Go to `VCS` > `Git` > `Push`.
   - If it's your first time pushing, you might need to define the remote repository. Click `Define Remote` and enter your GitHub repository URL (e.g., `https://github.com/username/Radahn.git`).
   - Click `Push`.

### Step-by-Step Procedure to Push to GitHub from VS Code

1. **Open Project in VS Code**:
   - Open your Radahn project in VS Code.

2. **Initialize Git Repository**:
   - Open the terminal in VS Code (Ctrl+`).
   - Run `git init` to initialize a Git repository.

3. **Add Files to Git**:
   - Run `git add .` to stage all the files.

4. **Commit Changes**:
   - Run `git commit -m "Initial commit"` to commit your changes with a message.

5. **Add Remote Repository**:
   - Run `git remote add origin https://github.com/username/Radahn.git` to add the remote repository.

6. **Push to GitHub**:
   - Run `git push -u origin master` to push your changes to GitHub.

Make sure to replace `username` with your actual GitHub username. You can continue adding more tools and functionality to the project and push the changes to GitHub as needed.
