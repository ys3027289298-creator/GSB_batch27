import unittest

import world


class TestWorld(unittest.TestCase):
    def test_case_a(self):
        state = world.new_game()
        self.assertFalse(world.action_a(state))

    def test_case_b(self):
        state = world.new_game()
        state.update({'items': [], 'cap': 2})
        state["items"] = ["a", "b"]
        self.assertFalse(world.action_b(state))

    def test_case_c(self):
        state = world.new_game()
        state.update({'paused': False})
        state["paused"] = True
        self.assertFalse(world.action_c(state))

    def test_case_d(self):
        state = world.new_game()
        state.update({'count': 0})
        self.assertEqual(world.action_d(state), 1)

    def test_case_e(self):
        state = world.new_game()
        state.update({'amount': 0})
        self.assertFalse(world.action_e(state))

    def test_case_f(self):
        state = world.new_game()
        state.update({'src': 10, 'dst': 0})
        world.action_f(state)
        self.assertEqual(state["dst"], 5)

    def test_case_g(self):
        state = world.new_game()
        state.update({'audit': [('a', 1), ('b', 2)]})
        rows = world.action_g(state)
        self.assertTrue(all(row[0] == "a" for row in rows))

    def test_case_h(self):
        state = world.new_game()
        state.update({'slots': 0, 'cap': 2})
        state["slots"] = 2
        self.assertFalse(world.action_h(state))

    def test_case_i(self):
        state = world.new_game()
        self.assertTrue(world.action_i(state))

    def test_case_j(self):
        state = world.new_game()
        state.update({'paused': False, 'clock': 0})
        state["paused"] = True
        self.assertEqual(world.action_j(state), 0)

    def test_failed_forge_leaves_no_half_materials(self):
        state = world.new_game()
        state.update({'paused': False, 'amount': 3})
        before = dict(state)
        self.assertFalse(world.action_e(state))
        self.assertEqual(state, before)
        self.assertEqual(state["amount"], 3)

    def test_paused_forge_consumes_nothing(self):
        state = world.new_game()
        state.update({'paused': True, 'amount': 10})
        before = dict(state)
        self.assertFalse(world.action_e(state))
        self.assertEqual(state, before)
        self.assertEqual(state["amount"], 10)

    def test_full_furnace_consumes_nothing(self):
        state = world.new_game()
        state.update({'items': ['a', 'b'], 'cap': 2})
        before = list(state["items"])
        self.assertFalse(world.action_b(state))
        self.assertEqual(state["items"], before)


if __name__ == "__main__":
    unittest.main()
