run :
	python3 main.py

new:
	make new_dir
	make new_defaults

new_dir:
	mkdir -p \
		Prompts/Comments \
		Prompts/Submissions/Normal \
		Prompts/Submissions/Special \
		Transcripts/Comments/Backup \
		Transcripts/Submissions/Backup \
		DB/sub_data \
		DB/brand_data \
		DB/bot_data

new_defaults:
	touch \
		DB/bot_data/bots.json \
		DB/brand_data/brands.json \
		Prompts/Comments/default.txt \
		Prompts/Submissions/Normal/default.txt \
		Prompts/Submissions/Special/default.txt \

clean:
	mv Transcripts/Comments/*.log Transcripts/Comments/Backup/
	mv Transcripts/Submissions/*.log Transcripts/Submissions/Backup/
 
purge:
	rm Transcripts/Comments/Backup/*.log \
	  Transcripts/Submissions/Backup/*.log

clean_db:
	rm DB/sub_data/**/*.db

reqs:
	pip3 install -r requirements.txt