import pygame
from pygame.locals import *
import sys

click = False
is_active = False
act = []
pygame.init()
timer = pygame.time.Clock()
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 1024
FM_SIZE = 20
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
main_font = pygame.font.SysFont("DejaVu Sans Mono", FM_SIZE)
ss = ["START", "STOP"]
ss_id = 0
game = 0
colors = [(77, 26, 0), (255, 204, 102), (0, 0, 102)]
btn_col = (102, 255, 51)
bcg_col = (0, 102, 0)
m_ft_col = (0, 127, 255)
n = 5
board = [[0 for i in range(n)] for j in range(n)]
eq = [0] * (n + 1)
eq[0] = 1
w_start = 650 - n * 50
h_start = 100
slot_size = 100
button_start = [1150, h_start]
gap = 2
button_size = [100, 50]
button_size_small = [10, 50]
button_center = button_start[0] + button_size[0] / 2
abort = 1


def end_check(event):
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        pygame.quit()
        sys.exit()


def is_safe(board, x, y, n):
    res = True
    for i in range(n):
        if board[x][i] == 2:
            res = False
        if board[i][y] == 2:
            res = False
    return res


def solve(board, n, r, placed, eq, ans):
    global act
    global abort
    if abort == 1:
        return
    if placed == r:
        if sorted(act) not in ans:
            ans.append(sorted(act))
            eq[r] += 1
            generate()
        return True
    for i in range(n):
        for j in range(n):
            if board[i][j] != 1:
                if is_safe(board, i, j, n):
                    board[i][j] = 2
                    act.append("{} {}".format(i, j))
                    solve(board, n, r, placed + 1, eq, ans)
                    board[i][j] = 0
                    act = act[:-1]

    return


def steer():
    global n
    global board
    global game
    global ss_id
    global click
    global click_y
    global click_x
    global abort
    for event in pygame.event.get():
        end_check(event)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
                click_x, click_y = event.pos

        if event.type == MOUSEBUTTONUP:
            click = False
            is_active = False


    if click:
        for i in range(n):
            for j in range(n):
                if w_start + slot_size * i <= click_x <= w_start + slot_size * (i + 1) \
                        and h_start + slot_size * j <= click_y <= h_start + slot_size * (j + 1):
                    board[i][j] = board[i][j] ^ 1
                    click = False
        # start
        if button_start[0] <= click_x <= button_start[0] + button_size[0] \
                and button_start[1] <= click_y <= button_start[1] + button_size[1]:
            game = game ^ 1
            abort = abort ^ 1
            click = False
        # clear
        if button_start[0] <= click_x <= button_start[0] + button_size[0] \
                and button_start[1] + 2 * button_size[1] <= click_y <= button_start[1] + 3 * button_size[1]:
            board = [[0 for i in range(n)] for j in range(n)]
            click = False
        # reverse
        if button_start[0] <= click_x <= button_start[0] + button_size[0] \
                and button_start[1] + 4 * button_size[1] <= click_y <= button_start[1] + 5 * button_size[1]:
            board = [[board[j][i] ^ 1 for i in range(n)] for j in range(n)]
            click = False
        # minus
        if button_start[0] <= click_x <= button_start[0] + 3 * button_size_small[0] - gap \
                and button_start[1] + 6 * button_size[1] <= click_y <= button_start[1] + 7 * button_size[1] \
                and n > 1:
            n -= 1
            board = [[0 for i in range(n)] for j in range(n)]
            eq = [0] * (n + 1)
            eq[0] = 1
            click = False
        # plus
        if button_start[0] + 7 * button_size_small[0] + gap <= click_x <= button_start[0] + 10 * button_size_small[0] \
                and button_start[1] + 6 * button_size[1] <= click_y <= button_start[1] + 7 * button_size[1] \
                and n < 9:
            n += 1
            eq = [0] * (n + 1)
            eq[0] = 1
            board = [[0 for i in range(n)] for j in range(n)]
            click = False


def generate():
    steer()
    window.fill(bcg_col)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                pygame.draw.rect(window, colors[(i + j) % 2],
                                 (w_start + slot_size * i, h_start + slot_size * j, slot_size, slot_size))
            elif board[i][j] == 1:
                pygame.draw.rect(window, colors[2],
                                 (w_start + slot_size * i, h_start + slot_size * j, slot_size, slot_size))
            else:
                pygame.draw.rect(window, colors[(i + j) % 2],
                                 (w_start + slot_size * i, h_start + slot_size * j, slot_size, slot_size))

    label = main_font.render(
        str(abort), False, m_ft_col)
    window.blit(label, (10, 150))
    '''label = main_font.render(str(click_y), False, m_ft_col)
    window.blit(label, (10, 200))
    for i in range(n):
        for j in range(n):
            label = main_font.render(str(board[i][j]), False, m_ft_col)
            window.blit(label, (100+20*i, 900+20*j))'''

    for i in range(n + 1):
        label = main_font.render(str(eq[i]), False, m_ft_col)
        window.blit(label, (50, h_start + 3*FM_SIZE*i))

    pygame.draw.rect(window, btn_col,
                     (button_start[0], button_start[1], button_size[0], button_size[1]))
    text_width = main_font.size(ss[game])[0]
    label = main_font.render(ss[game], False, m_ft_col)
    window.blit(label,
                (button_center - (text_width / 2), button_start[1] + 0.5 * button_size[1] - FM_SIZE / 2))

    pygame.draw.rect(window, btn_col,
                     (button_start[0], button_start[1] + 2 * button_size[1], button_size[0], button_size[1]))
    text_width = main_font.size("Clear")[0]
    label = main_font.render("Clear", False, m_ft_col)
    window.blit(label,
                (button_center - (text_width / 2), button_start[1] + 2.5 * button_size[1] - FM_SIZE / 2))

    pygame.draw.rect(window, btn_col,
                     (button_start[0], button_start[1] + 4 * button_size[1], button_size[0], button_size[1]))
    text_width = main_font.size("Reverse")[0]
    label = main_font.render("Reverse", False, m_ft_col)
    window.blit(label,
                (button_center - (text_width / 2), button_start[1] + 4.5 * button_size[1] - FM_SIZE / 2))
    if n > 1:
        pygame.draw.rect(window, btn_col,
                         (button_start[0], button_start[1] + 6 * button_size[1],
                          3 * button_size_small[0] - gap, button_size_small[1]))
        text_width = main_font.size("-")[0]
        label = main_font.render("-", False, m_ft_col)
        window.blit(label,
                    (button_start[0] + (3 * button_size_small[0] - gap) / 2 - (text_width / 2),
                     button_start[1] + 6.5 * button_size[1] - FM_SIZE / 2))

    pygame.draw.rect(window, btn_col,
                     (button_start[0] + 3 * button_size_small[0], button_start[1] + 6 * button_size[1],
                      4 * button_size_small[0], button_size_small[1]))
    text_width = main_font.size(str(n))[0]
    label = main_font.render(str(n), False, m_ft_col)
    window.blit(label,
                (button_center - (text_width / 2), button_start[1] + 6.5 * button_size[1] - FM_SIZE / 2))
    if n < 9:
        pygame.draw.rect(window, btn_col,
                         (button_start[0] + 7 * button_size_small[0] + gap, button_start[1] + 6 * button_size[1],
                          3 * button_size_small[0] - gap, button_size_small[1]))
        text_width = main_font.size("+")[0]
        label = main_font.render("+", False, m_ft_col)
        window.blit(label,
                    (button_start[0] + 7 * button_size_small[0] + gap + (3 * button_size_small[0] - gap) / 2 - (
                            text_width / 2),
                     button_start[1] + 6.5 * button_size[1] - FM_SIZE / 2))
    timer.tick(10000)
    pygame.display.flip()


while True:

    w_start = 650 - n * 50

    if game == 1:
        abort = 0
        eq = [0] * (n + 1)
        eq[0] = 1
        for r in range(1, n + 1):
            solve(board, n, r, 0, eq, [])
        abort = 1
        game = 0
    generate()

