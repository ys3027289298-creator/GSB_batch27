import unittest

import engine


class TestEngine(unittest.TestCase):
    def test_case_a(self):
        state = engine.new_game()
        self.assertFalse(engine.rule_a(state))

    def test_case_b(self):
        state = engine.new_game()
        state.update({'events': {1: True}})
        engine.rule_b(state)
        self.assertNotIn(1, state["events"])

    def test_case_c(self):
        state = engine.new_game()
        state.update({'used': 1, 'cap': 2})
        self.assertEqual(engine.rule_c(state), 1)

    def test_case_d(self):
        state = engine.new_game()
        self.assertFalse(engine.rule_d(state))

    def test_case_e(self):
        state = engine.new_game()
        state.update({'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}})
        engine.rule_e(state)
        self.assertNotIn((1, 2), state["edges"])

    def test_case_f(self):
        state = engine.new_game()
        self.assertIsNone(engine.rule_f(state))

    def test_case_g(self):
        state = engine.new_game()
        state.update({'queue': []})
        state["queue"] = [1]
        self.assertEqual(engine.rule_g(state), 1)
        self.assertEqual(len(state["queue"]), 1)

    def test_case_h(self):
        state = engine.new_game()
        state.update({'count': 0})
        state["count"] = 5
        engine.rule_h(state)
        self.assertEqual(state["count"], 0)

    def test_case_i(self):
        state = engine.new_game()
        state.update({'balance': 10})
        self.assertFalse(engine.rule_i(state))
        self.assertEqual(state["balance"], 10)

    def test_case_j(self):
        state = engine.new_game()
        state.update({'accounts': {}})
        self.assertEqual(engine.rule_j(state), 0)

    def test_invariants_clean_state(self):
        state = engine.new_game()
        state.update({
            'used': 1, 'cap': 2, 'balance': 30, 'count': 0,
            'queue': [1], 'nodes': {1: True, 2: True},
            'edges': {(1, 2): 5}, 'events': {}, 'accounts': {},
        })
        self.assertEqual(engine.invariants(state), [])

    def test_invariants_detect_violations(self):
        state = engine.new_game()
        state.update({
            'used': 3, 'cap': 2, 'balance': -5, 'count': -1,
            'nodes': {2: True}, 'edges': {(1, 2): 5},
        })
        problems = engine.invariants(state)
        self.assertEqual(len(problems), 4)

    def test_replay_verifies_sequence(self):
        state = engine.new_game()
        state.update({
            'used': 1, 'cap': 2, 'balance': 30, 'count': 5,
            'queue': [1], 'nodes': {1: True, 2: True},
            'edges': {(1, 2): 5}, 'events': {1: True}, 'accounts': {},
        })
        engine.replay(state, list("abcdefghij"))
        self.assertEqual(engine.invariants(state), [])
        self.assertEqual(state["count"], 0)
        self.assertEqual(state["balance"], 10)
        self.assertEqual(state["queue"], [1])
        self.assertNotIn(1, state["events"])
        self.assertEqual(state["edges"], {})

    def test_replay_rejects_invalid_initial_state(self):
        state = engine.new_game()
        state.update({'used': 5, 'cap': 2})
        with self.assertRaises(AssertionError):
            engine.replay(state, [])


if __name__ == "__main__":
    unittest.main()
