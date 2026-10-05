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


class TestInvariants(unittest.TestCase):
    def test_new_game_satisfies_invariants(self):
        self.assertTrue(engine.check_invariants(engine.new_game()))

    def test_fuel_invariant(self):
        self.assertTrue(engine.check_invariants({'used': 1, 'cap': 2}))
        with self.assertRaises(ValueError):
            engine.check_invariants({'used': 3, 'cap': 2})

    def test_balance_invariant(self):
        with self.assertRaises(ValueError):
            engine.check_invariants({'balance': -1})

    def test_count_invariant(self):
        with self.assertRaises(ValueError):
            engine.check_invariants({'count': -1})

    def test_edge_endpoint_invariant(self):
        self.assertTrue(engine.check_invariants(
            {'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}}))
        with self.assertRaises(ValueError):
            engine.check_invariants({'nodes': {2: True}, 'edges': {(1, 2): 5}})

    def test_rules_preserve_invariants(self):
        state = {
            'events': {1: True},
            'nodes': {1: True, 2: True},
            'edges': {(1, 2): 5},
            'used': 1, 'cap': 2,
            'queue': [1],
            'count': 5,
            'balance': 100,
            'accounts': {},
        }
        for op in (engine.rule_b, engine.rule_e, engine.rule_g,
                   engine.rule_h, engine.rule_i):
            op(state)
            self.assertTrue(engine.check_invariants(state))


class TestReplay(unittest.TestCase):
    def _initial_state(self):
        return {
            'events': {1: True},
            'nodes': {1: True, 2: True},
            'edges': {(1, 2): 5},
            'used': 1, 'cap': 2,
            'queue': [1],
            'count': 5,
            'balance': 100,
            'accounts': {},
        }

    def test_replay_matches_live_run(self):
        ops = [engine.rule_b, engine.rule_e, engine.rule_h, engine.rule_i]
        live = self._initial_state()
        for op in ops:
            op(live)
        self.assertTrue(engine.verify_replay(self._initial_state(), ops, live))

    def test_replay_is_deterministic(self):
        ops = [engine.rule_b, engine.rule_e, engine.rule_h, engine.rule_i]
        first = engine.replay(self._initial_state(), ops)
        second = engine.replay(self._initial_state(), ops)
        self.assertEqual(first, second)

    def test_replay_does_not_mutate_input(self):
        state = self._initial_state()
        snapshot = dict(state)
        engine.replay(state, [engine.rule_b, engine.rule_h, engine.rule_i])
        self.assertEqual(state, snapshot)

    def test_replay_enforces_invariants(self):
        def bad_op(s):
            s['balance'] = -1
        with self.assertRaises(ValueError):
            engine.replay({'balance': 10}, [bad_op])


if __name__ == "__main__":
    unittest.main()
