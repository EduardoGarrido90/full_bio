mkdir experiments
for ((i=1;i<=100;i+=1)); do
	echo $i
	mkdir experiments/exp_${i}
	cp -r base_folder/* experiments/exp_${i}/

	sed -i -- "s/\"random_seed\"     : 1/\"random_seed\"     : ${i}/g" experiments/exp_${i}/ga/config.json
	sed -i -- "s/\"random_seed\"     : 1/\"random_seed\"     : ${i}/g" experiments/exp_${i}/pes/config.json
	sed -i -- "s/\"random_seed\"     : 1/\"random_seed\"     : ${i}/g" experiments/exp_${i}/random/config.json

	sed -i -- "s/\"experiment-name\" : \"simple_ga_rosenbrock_ei_1\"/\"experiment-name\" : \"simple_ga_rosenbrock_ei_${i}\"/g" experiments/exp_${i}/ga/config.json
	sed -i -- "s/\"experiment-name\" : \"simple_ga_rosenbrock_pes_1\"/\"experiment-name\" : \"simple_ga_rosenbrock_pes_${i}\"/g" experiments/exp_${i}/pes/config.json
	sed -i -- "s/\"experiment-name\" : \"simple_ga_rosenbrock_random_1\"/\"experiment-name\" : \"simple_ga_rosenbrock_random_${i}\"/g" experiments/exp_${i}/random/config.json

	(cd experiments/exp_${i}/ga/ && sbatch -p cccmd -A ada2_serv --exclude=depaz05 ./script_cluster.sh)
	(cd experiments/exp_${i}/pes/ && sbatch -p cccmd -A ada2_serv --exclude=depaz05 ./script_cluster.sh)
	(cd experiments/exp_${i}/random/ && sbatch -p cccmd -A ada2_serv --exclude=depaz05 ./script_cluster.sh)
done
