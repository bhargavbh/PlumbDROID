## PlumbDROID

This is a replication package for the submission titled "Automated Repair of Resource Leaks in Android Applications" to TSE 2021.
https://arxiv.org/abs/2003.03201

The package contains the tool PlumbDROID and the accompanying data for experiments in the paper

# PlumbDROID (Tool)

This is a tool for static detection and repair of resource leaks in Android apps. The tool takes as input apk of an app and produces patches (for leaks) at the level of smali which
which can be recompiled into

### How to install
**0. Requirements**
- PlumbDROID has a following major dependencies:
  $ Androguard 3.3.5 (https://pypi.org/project/androguard/)
  $ Apktool 2.0.0 (https://ibotpeaches.github.io/Apktool/install/)
  $ Android SDK along with Android Studio to run tests.

**1. Install Androguard **
- ```pip install -U androguard```

**2. Install Apktool **
- procedure described for MacOS
  $ Download Mac wrapper script (Right click, Save Link As apktool)
  $ Download apktool-2 (find newest here)
  $ Rename downloaded jar to apktool.jar
  $ Move both files (apktool.jar & apktool) to /usr/local/bin (root needed)
  $ Make sure both files are executable (chmod +x)


**3. Install Android SDK** (go to next step if you already have it)
The next steps will allow you to install Android SDK in Non-GUI mode:
- Download and unzip Android SDK:
    ```sh
    $ cd
    $ wget http://dl.google.com/android/android-sdk_r24.2-macos.tgz
    $ tar -xvf android-sdk_r24.2-macos.tgz
    ```

- Add Android SDK to path (if you don't use Bash i.e. you prefer Zsh, remember to modify the correct file). To to that, add these two lines to your `~/.bashrc` file:
    ```
    export ANDROID_HOME=$HOME/android-sdk-linux/
    export PATH=$PATH:$ANDROID_HOME/tools
    export PATH=$PATH:$ANDROID_HOME/platform-tools
    ```
- Load the libraries in the current session with:

    ```sh
    $ source ~/.bashrc
    ```
- NOTE: If you need to run PlumbDroid on apps following the manifestation file design prior to Android 7.3.2,
  use Android Studio with a different xml parser: version 1.4 or prior.

**3. Prepare PlumbDROID**

- We need to give the necessary permissions to all the scripts
    ```sh
    $ chmod 744 PlumbDROID/*.sh
    ```

**4. Install the Python libraries required**

- The following Python libraries are required:
    ```sh
    $ pip install -r PlumbDROID/requirements.txt
    ```
**5. Now we can run PlumbDROID**
- If everything was OK, we can now run PlumbDROID:
    ```sh
    $ cd PlumbDROID/
    $ python PlumbDROID.py -s </PATH/TO/FOLDER/WITH/APKS/>
    ```

## Input and output folder structure

**INPUT:** A folder containing files with ".apk" extension.
**OUTPUT:** A structure of folders following this scheme:

# /                     --> root folder
# /plumbDroid_outputs/   --> plumbdroid results
# /plumbDroid_outputs/patched_apps --> patched apks for each of resources
# /plumbDroid_outputs/patches --> plumbdroid generated patches in smali with location
# /metrics/      --> Features files generated with PlumbDROID

### Usage

usage: python PlumbDROID.py [-d] [-r] [-rfg] </PATH/TO/FOLDER/WITH/APKS/> -o  </PATH/TO/OUTPUT/FOLDER/>


optional arguments:

 -r ResourceList, --resourcelist LIST
                       Change the resources being analysed; List to be added separated by commands.
                       By default all resources are analysed. The supported list of resources are:
                       AudioRecorder
                       BluetoothAdapter
                       Camera
                       LocationListener
                       MediaPlayer
                       Vibrator
                       WakeLock
                       WifiLock
                       WifiManager

                       If you intend to add other pairs of acquire-release operations, please modify the
                       file xml/resources.xml in the format adherent to other pairs.


 -d UnrollingDepth [Depth ...], --depth Depth
                       Parameter sets the number of unrolling of loops in call-back graphs.
                       Note d > 6 will drastically slow down analysis time.
 -rfg, --ResourceFlowGraph
                       Additionally generate intermediary resourceflowgraphs
 -o FOLDER, --output FOLDER
                       Specify Output folder

## Structure of Replication Package

The file Sheet-1 and 2 of PlumbDROID_Results.xlsx contains data associated with tables-3,4, anf 5 in the paper.
Sheet-3 contains a detailed report of all the leaks found by PlumbDROID along with the location of buggy method, extent of leak and the
minimum unrolling-depth (d) required for leak detection.

There is one folder for each of the benchmarks titled DroidLeaks_result, Relda2_result and Relfix_results.
They contain the original apks, patched apks and also the list of PlumDROID patches in smali generated per app in the files
app_name.smali. Within the file, the following convention is used:

'------' : demarcates patched_apps
'******' : demarcates metadata associated with patch like location, depth, etc.
'######' : demarcates different resources
