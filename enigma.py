class enigma():
    def __init__(self):
        # self.rotor I
        self.rotor_I = {
            0: 4, 1: 10, 2: 12, 3: 5, 4: 11, 5: 6, 6: 3, 7: 16, 8: 21, 9: 25, 10: 13,
            11: 19, 12: 14, 13: 22, 14: 24, 15: 7, 16: 23, 17: 20, 18: 18, 19: 15, 20: 0,
            21: 8, 22: 1, 23: 17, 24: 2, 25: 9
        }

        # self.rotor II
        self.rotor_II = {
            0: 0, 1: 9, 2: 3, 3: 10, 4: 18, 5: 8, 6: 17, 7: 20, 8: 23, 9: 1, 10: 11,
            11: 7, 12: 22, 13: 19, 14: 12, 15: 2, 16: 16, 17: 6, 18: 25, 19: 13, 20: 15,
            21: 24, 22: 5, 23: 21, 24: 14, 25: 4
        }

        # self.rotor III
        self.rotor_III = {
            0: 1, 1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 2, 7: 15, 8: 17, 9: 19, 10: 23,
            11: 21, 12: 25, 13: 13, 14: 24, 15: 4, 16: 8, 17: 22, 18: 6, 19: 0, 20: 10,
            21: 12, 22: 20, 23: 18, 24: 16, 25: 14
        }

        self.rotor_list = [self.rotor_I, self.rotor_II, self.rotor_III]

        # Reflector B
        self.reflector_B = {
            0: 24, 1: 17, 2: 20, 3: 7, 4: 16, 5: 18, 6: 11, 7: 3, 8: 15, 9: 23, 10: 13,
            11: 6, 12: 14, 13: 10, 14: 12, 15: 8, 16: 4, 17: 1, 18: 5, 19: 25, 20: 2,
            21: 22, 22: 21, 23: 9, 24: 0, 25: 19
        }

        self.position = [0, 0, 0]

    def set_rotor_pos(self):
        for i in range(len(self.position)):
            for j in range(self.position[i]):
                self.rotate_rotor(self.rotor_list[i])

    def rotation(self):
        first = self.position[0]
        second = self.position[1]
        third = self.position[2]

        first += 1
        self.rotate_rotor(self.rotor_I)

        if first == 26:
            first = 0
            second += 1
            self.rotate_rotor(self.rotor_II)
        
            if second == 26:
                second = 0
                third += 1
                self.rotate_rotor(self.rotor_III)

                if third == 26:
                    third = 0

        self.position = [first, second, third]

    def rotate_rotor(self, rotor):
        first_value = rotor[0]
        for i in range(25):
            rotor[i] = rotor[i + 1]
        rotor[25] = first_value

    def forward(self, number):
        for i in range(3): 
            number = self.rotor_list[i][number]
        
        number = self.reflector_B[number]
        return self.backward(number)
    
    def backward(self, number):
        for i in range(2, -1, -1):
            for key, val in self.rotor_list[i].items():
                if val == number:
                    number = key
                    break
        
        return number