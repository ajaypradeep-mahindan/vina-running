#this program is to run the autodock vina to run the multiple ligand docking 




import os

def run_autodock_vina(vina_executable, receptor_pdbqt, ligand_pdbqt, output_dir, config):
    ligand_name = os.path.splitext(os.path.basename(ligand_pdbqt))[0]#to get the ligand filename 
    output_file = os.path.join(output_dir, f"{ligand_name}_result.pdbqt")#to save the output file corresopnding to each ligand 
    log_file = os.path.join(output_dir, f"{ligand_name}_log.txt")# to save the log file of each binding scores corresponding to each ligand 
    
    command = f"{vina_executable} --receptor {receptor_pdbqt} --ligand {ligand_pdbqt} --out {output_file} --config {config} --log {log_file}"
    os.system(command)

def run_autodock_vina_for_multiple_ligands(vina_executable, receptor_pdbqt, ligand_dir, output_dir, config):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)# creates output folder if it doesnt exist

    ligands = [f for f in os.listdir(ligand_dir) if f.endswith(".pdbqt")]

    if not os.path.exists(vina_executable) or not os.access(vina_executable, os.X_OK):
        print("AutoDock Vina executable not found or not executable. Please install Vina and provide the correct path.") #to verify the installation exist 
        exit()

    for ligand in ligands:
        ligand_path = os.path.join(ligand_dir, ligand)
        run_autodock_vina(vina_executable, receptor_pdbqt, ligand_path, output_dir, config)

if __name__ == "__main__":
    vina_executable = "/path/to/vina"  #  path to your AutoDock Vina executable on Linux
    receptor_pdbqt = "/path/to/receptor.pdbqt"  #  path to your receptor PDBQT file
    config = "/path/to/config.txt"  #  path to your configuration file
    ligand_dir = "/path/to/ligands"  # path to your ligands directory
    output_dir = "/path/to/output"  # desired output directory

    run_autodock_vina_for_multiple_ligands(vina_executable, receptor_pdbqt, ligand_dir, output_dir, config)
