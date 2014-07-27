import pygame

def process_events():
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True  # Flag that we are done so we exit this loop
            # --- Game logic should go here
            # --- Drawing code should go here
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            screen.fill(WHITE)
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True  # Flag that we are done so we exit this loop
                screen.fill(WHITE)
                pygame.display.flip()
                pygame.quit()
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            newUnit = Barbarian()
            newUnit.pos_3d[0] = pos[0] / PIXELS_PER_SPACE
            newUnit.pos_3d[1] = pos[1] / PIXELS_PER_SPACE
            if event.button == 1:
                newUnit.fill = 1
                attackingList.append(newUnit)
            elif event.button == 3:
                defendingList.append(newUnit)
    return done

