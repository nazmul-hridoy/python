{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " | | \n",
      "-|-|-\n",
      " | | \n",
      "-|-|-\n",
      " | | \n"
     ]
    }
   ],
   "source": [
    "from IPython.display import clear_output\n",
    "def display_board(board):\n",
    "    print(board[7] + '|' +board[8] + '|' +board[9])\n",
    "    print('-|-|-')\n",
    "    print(board[4] + '|' +board[5] + '|' +board[6])\n",
    "    print('-|-|-')\n",
    "    print(board[1] + '|' +board[2] + '|' +board[3])\n",
    "test_board = [' '] * 10\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PLAYER 1, SELECT X OR O: X\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('X', 'O')"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def player_input():\n",
    "    \n",
    "    marker = ' '\n",
    "    while marker != 'X' and marker != 'O':\n",
    "        marker = input('PLAYER 1, SELECT X OR O: ').upper()\n",
    "    player1 = marker\n",
    "    player2 = ' '\n",
    "    if player1 == 'X':\n",
    "        player2 = 'O'\n",
    "    else:\n",
    "        player2 = 'X'\n",
    "    return(player1,player2)\n",
    "player_input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " |#| \n",
      "-|-|-\n",
      " | | \n",
      "-|-|-\n",
      " | | \n"
     ]
    }
   ],
   "source": [
    "def place_marker(board,marker,position):\n",
    "    board[position] = marker\n",
    "place_marker(test_board, '#', 8)\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board,mark):\n",
    "    \n",
    "    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top\n",
    "    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle\n",
    "    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom\n",
    "    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle\n",
    "    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle\n",
    "    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side\n",
    "    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal\n",
    "    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def choose_first():\n",
    "    if random.randint(0, 1) == 0:\n",
    "        return 'Player 2'\n",
    "    else:\n",
    "        return 'Player 1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def space_check(board, position):\n",
    "    \n",
    "    return board[position] == ' '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_board_check(board):\n",
    "    for i in range(1,10):\n",
    "        if space_check(board, i):\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_choice(board):\n",
    "    position = 0\n",
    "    \n",
    "    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):\n",
    "        position = int(input('Choose your next position: (1-9) '))\n",
    "        \n",
    "    return position"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def replay():\n",
    "    \n",
    "    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Tic Tac Toe!\n",
      "PLAYER 1, SELECT X OR O: X\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'choose_first' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-6c79884158f8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mtheBoard\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;34m' '\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m*\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mplayer1_marker\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mplayer2_marker\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mplayer_input\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m     \u001b[0mturn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mchoose_first\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mturn\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m' will go first.'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'choose_first' is not defined"
     ]
    }
   ],
   "source": [
    "print('Welcome to Tic Tac Toe!')\n",
    "\n",
    "while True:\n",
    "    # Reset the board\n",
    "    theBoard = [' '] * 10\n",
    "    player1_marker, player2_marker = player_input()\n",
    "    turn = choose_first()\n",
    "    print(turn + ' will go first.')\n",
    "    \n",
    "    play_game = input('Are you ready to play? Enter Yes or No.')\n",
    "    \n",
    "    if play_game.lower()[0] == 'y':\n",
    "        game_on = True\n",
    "    else:\n",
    "        game_on = False\n",
    "\n",
    "    while game_on:\n",
    "        if turn == 'Player 1':\n",
    "            # Player1's turn.\n",
    "            \n",
    "            display_board(theBoard)\n",
    "            position = player_choice(theBoard)\n",
    "            place_marker(theBoard, player1_marker, position)\n",
    "\n",
    "            if win_check(theBoard, player1_marker):\n",
    "                display_board(theBoard)\n",
    "                print('Congratulations! You have won the game!')\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(theBoard):\n",
    "                    display_board(theBoard)\n",
    "                    print('The game is a draw!')\n",
    "                    break\n",
    "                else:\n",
    "                    turn = 'Player 2'\n",
    "\n",
    "        else:\n",
    "            # Player2's turn.\n",
    "            \n",
    "            display_board(theBoard)\n",
    "            position = player_choice(theBoard)\n",
    "            place_marker(theBoard, player2_marker, position)\n",
    "\n",
    "            if win_check(theBoard, player2_marker):\n",
    "                display_board(theBoard)\n",
    "                print('Player 2 has won!')\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(theBoard):\n",
    "                    display_board(theBoard)\n",
    "                    print('The game is a draw!')\n",
    "                    break\n",
    "                else:\n",
    "                    turn = 'Player 1'\n",
    "\n",
    "    if not replay():\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
