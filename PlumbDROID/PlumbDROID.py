import os
import sys
import shutil
import argparse

from time import sleep
from os import listdir
from termcolor import colored
from os.path import join as join_dir
from argparse import RawTextHelpFormatter

from aux_functions import filter_valid_apks
from aux_functions import analyse_plumbdroid
from aux_functions import filter_apks
from CFG-gen import run_cfg_generator
from ResourceFlowGraph import process_rfgs
from plumbdroid import analyze_with_plumbdroid

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

os.chdir(CURRENT_DIRECTORY)


def main():

    parser = argparse.ArgumentParser(
        description=colored("Welcome to plumbdroid\n\n") + " You must provide the source directory where apks are contained.",
        formatter_class=RawTextHelpFormatter)

    
    parser.add_argument('-r', '--resource', default='all', help='Resource List to be analysed', required=True)

    parser.add_argument('-d', '--depth', default=3,
                        help='Unrolling Depth of the CallBack Graph in the analysis',
                        action='store_true')

    parser.add_argument('-f', '--filter', help='Filter valid and invalid Apks (Recommended).', default=True,
                        required=False, action='store_true')

       parser.add_argument('-rfg', '--ResourceFlowGraph', help='Exports the RFGs generated to a .gml graph format.', default=True,
                        required=False              )

    parser.add_argument('-o', '--output_folder', default="/Output", required=False, help='Output Folder')


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    source_folder = args.source

    step_filter_apks = True
    step_analyse_virus_total = args.virustotal_api_key
    step_filter_bw_mw = True
    step_run_plumbdroid = True
    step_run_plumbdroid = True

    if not args.allsteps:
        step_filter_apks = args.filter
        step_analyse_virus_total = args.virustotal_api_key
        step_filter_bw_mw = args.classify
        step_run_plumbdroid = args.plumbdroid
        step_run_plumbdroid = args.plumbdroid

   
    execute_plumdroid_tool(source_folder=source_folder,
                                step_filter_apks=step_filter_apks,
                                step_filter_bw_mw=step_filter_bw_mw,
                                step_run_plumbdroid=step_run_plumbdroid,
                                step_run_plumbdroid=step_run_plumbdroid,
                                save_single_analysis=args.single,
                                perform_nocleanup=args.nocleanup,
                                package_index=args.packageIndex,
                                class_index=args.classIndex,
                                system_commands_index=args.systemCommandsIndex,
                                export_mongodb=args.mongodbURI,
                                exportCSV=args.exportCSV,
                                with_color=args.color,
                                vt_threshold=args.virustotal_threshold,
                                plumbdroid_time=args.plumbdroid_time,
                                virus_total_api_key=step_analyse_virus_total
                                )


def print_message(message, with_color, color):
    if with_color:
        print colored(message, color)
    else:
        print message


def execute_andro_py_tool_steps(source_folder, step_filter_apks, ,
                                step_run_plumbdroid, step_run_plumbdroid, save_single_analysis, perform_nocleanup,
                                package_index, class_index, system_commands_index, export_mongodb, exportCSV,
                                with_color, vt_threshold, plumbdroid_time, virus_total_api_key=None):
    if step_filter_apks:
        print_message("\n\n>>>> PlumbDroid -- STEP 1: Filtering apks\n")
       
        filter_valid_apks(source_directory=source_folder,
                          valid_apks_directory=join_dir(source_folder, APKS_DIRECTORY),
                          invalid_apks_directory=join_dir(source_folder, INVALID_APKS_DIRECTORY),
                          with_color=with_color)

        sleep(1)

    else:
        
        if not os.path.exists(join_dir(source_folder, APKS_DIRECTORY)):
            os.makedirs(join_dir(source_folder, APKS_DIRECTORY))

        list_apks = [f for f in listdir(source_folder) if f.endswith(".apk")]
        for apk in list_apks:
            shutil.move(join_dir(source_folder, apk), join_dir(source_folder, APKS_DIRECTORY, apk))

    if plumbroid_apk_key is not None:
        print_message("\n\n>>>> PlumbDroid- analysing with given depth")

        analyse_virustotal(source_directory=join_dir(source_folder, APKS_DIRECTORY),
                           vt_analysis_output_folder=join_dir(source_folder, VIRUSTOTAL_FOLDER),
                           output_samples_folder=join_dir(source_folder, APKS_DIRECTORY),
                           with_color=with_color, vt_api_key=virus_total_api_key)

        sleep(1)

  
    if step_filter_bw_mw:
        print_message("Preparing patches")

        filter_apks(source_directory=join_dir(source_folder, APKS_DIRECTORY),
                    vt_analysis_directory=join_dir(source_folder, VIRUSTOTAL_FOLDER),
                    bw_directory_name=join_dir(source_folder, BW_DIRECTORY),
                    mw_directory_name=join_dir(source_folder, MW_DIRECTORY),
                    threshold=vt_threshold)

        sleep(1)

    if step_run_plumbdroid:
                print_message("\n\n>>>> PlumbDroid- validating the patch")

        run_plumbdroid(source_directory=join_dir(source_folder, APKS_DIRECTORY),
                      output_folder=join_dir(source_folder, plumbdroid_RESULTS_FOLDER),
                      with_color=with_color)

        sleep(1)

    if step_run_plumbdroid:
        print_message("\n\n>>>> plumbdroid -- STEP 5: Processing plumbdroid outputs\n", with_color, "green")

        process_plumbdroid_outputs(plumbdroid_analyses_folder=join_dir(source_folder, plumbdroid_RESULTS_FOLDER),
                                  output_folder_individual_csv=join_dir(source_folder, plumbdroid_PROCESSED_FOLDER),
                                  output_csv_file=join_dir(source_folder, plumbdroid_PROCESSED_FOLDER,
                                                           OUTPUT_GLOBAL_FILE_plumbdroid),
                                  with_color=with_color)

        sleep(1)

    if step_run_plumbdroid:


    print_message("\n\n>>>> plumbdroid -- STEP 7: Execute leak analysis\n", with_color, "green")

    apk_analysis(apks_directory=join_dir(source_folder, APKS_DIRECTORY),
                       single_analysis=save_single_analysis,
                       dynamic_analysis_folder=join_dir(source_folder, DYNAMIC_ANALYSIS_FOLDER),
                       virus_total_reports_folder=join_dir(source_folder, VIRUSTOTAL_FOLDER),
                       plumbdroid_folder=join_dir(source_folder, plumbdroid_PROCESSED_FOLDER),
                       output_folder=join_dir(source_folder, FEATURES_FILES),
                       noclean_up=perform_nocleanup,
                       package_index_file=package_index,
                       classes_index_file=class_index,
                       system_commands_file=system_commands_index,
                       label=None,
                       avclass=True,
                       export_csv=exportCSV)


if __name__ == '__main__':
    main()
