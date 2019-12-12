import functions

game_manager_1 = functions.game_manager()

def test_check_ate_poison():
    game_manager_1.p_snake.make_move('d')
    game_manager_1.p_snake.make_move('s')
    assert game_manager_1.check_ate_poison() == True

    
def test_spawn_poison():
    game_manager_1.spawn_poison()
    assert 'P' in game_manager_1.game_grid()
    
