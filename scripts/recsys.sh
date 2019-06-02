cd ../src

THEANO_FLAGS=mode=FAST_RUN,device=cuda python train_hier_gru.py recsys-dense lso-test 100 100 \
--loss top1 --hidden_act tanh \
--user_propagation_mode all --user_to_output 0 \
--adapt adagrad --learning_rate 0.1 --momentum 0.2 --batch_size 2 \
--dropout_p_hidden_usr 0.1 \
--dropout_p_hidden_ses 0.1 \
--dropout_p_init 0.2 \
--n_epochs 100 --train_random_order 0 \
--eval_cutoff 5 \
--user_key user_id --item_key item_id --session_key session_id --time_key created_at \
--rnd_seed 1
