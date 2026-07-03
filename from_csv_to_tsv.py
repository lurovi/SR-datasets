import pandas as pd
import gzip
import shutil


def main():
    dataset_names = ['airfoil.csv', 'blackbox_1028_SWD.csv', 'blackbox_1089_USCrime.csv', 'blackbox_1193_BNG_lowbwt.csv', 'blackbox_1199_BNG_echoMonths.csv', 'blackbox_192_vineyard.csv', 'blackbox_210_cloud.csv', 'blackbox_522_pm10.csv', 'blackbox_557_analcatdata_apnea1.csv', 'blackbox_579_fri_c0_250_5.csv', 'blackbox_606_fri_c2_1000_10.csv', 'blackbox_650_fri_c0_500_50.csv', 'blackbox_678_visualizing_environmental.csv', 'concrete.csv', 'dummy.csv', 'firstprinciples_absorption.csv', 'firstprinciples_bode.csv', 'firstprinciples_hubble.csv', 'firstprinciples_ideal_gas.csv', 'firstprinciples_kepler.csv', 'firstprinciples_leavitt.csv', 'firstprinciples_newton.csv', 'firstprinciples_planck.csv', 'firstprinciples_rydberg.csv', 'firstprinciples_schechter.csv', 'firstprinciples_supernovae_zr.csv', 'firstprinciples_tully_fisher.csv', 'istanbul.csv', 'keijzer6.csv', 'nguyen7.csv', 'pagie1.csv', 'parkinson.csv', 'qsaraquatic.csv', 'slump.csv', 'toxicity.csv', 'vladislavleva4.csv', 'yacht.csv']
    
    for dataset in dataset_names:
        df = pd.read_csv(dataset)
        df = df.rename({'y': 'target'}, axis=1, inplace=False)
        print(df.head())
        df.to_csv(f'srbench_format/{dataset.replace(".csv", "")}.tsv', sep='\t', index=False)
        with open(f'srbench_format/{dataset.replace(".csv", "")}.tsv', 'rb') as f_in:
            with gzip.open(f'srbench_format/{dataset.replace(".csv", "")}.tsv.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    main()

