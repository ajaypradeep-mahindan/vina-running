import os

def run_autodock_vina(vina_executable, receptor_pdbqt, ligand_pdbqt, output_dir, config):
    ligand_name = os.path.splitext(os.path.basename(ligand_pdbqt))[0]
    output_file = os.path.join(output_dir, f"{ligand_name}_result.pdbqt")
    log_file = os.path.join(output_dir, f"{ligand_name}_log.txt")
    
    command = f"{vina_executable} --receptor {receptor_pdbqt} --ligand {ligand_pdbqt} --out {output_file} --config {config} --log {log_file}"
    os.system(command)

def run_autodock_vina_for_multiple_ligands(vina_executable, receptor_pdbqt, ligand_dir, output_dir, config):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ligands = [f for f in os.listdir(ligand_dir) if f.endswith(".pdbqt")]

    for ligand in ligands:
        ligand_path = os.path.join(ligand_dir, ligand)
        run_autodock_vina(vina_executable, receptor_pdbqt, ligand_path, output_dir, config)

if __name__ == "__main__":
    vina_executable = "D:/runVina/vina.exe"  # Update with the path to your AutoDock Vina executable
    receptor_pdbqt = "D:/runVina/4bfs.pdbqt"  # Update with the path to your receptor PDBQT file
    config = "D:/runVina/config4.txt"  # Update with the path to your configuration file
    ligand_dir = "D:/runVina/ligands"  # Update with the path to your ligands directory
    output_dir = "D:/runVina/opf"  # Update with the desired output directory

    run_autodock_vina_for_multiple_ligands(vina_executable, receptor_pdbqt, ligand_dir, output_dir, config)
