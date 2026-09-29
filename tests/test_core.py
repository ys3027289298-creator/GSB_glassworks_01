import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_load(self):
        state = core.new_game()
        self.assertTrue(core.load_kiln(state, 1))
        self.assertFalse(core.load_kiln(state, 1))

    def test_02_kiln_capacity(self):
        state = core.new_game()
        state["kiln_load"] = 2
        result = core.load_kiln(state, 1)
        self.assertFalse(result)

    def test_03_temp_boundary(self):
        state = core.new_game()
        self.assertEqual(core.check_temp(state, 35), "over")

    def test_04_cancel_releases_kiln(self):
        state = core.new_game()
        core.load_kiln(state, 1)
        core.cancel(state, 1)
        self.assertEqual(state["kiln_load"], 0)

    def test_05_no_draw_without_material(self):
        state = core.new_game()
        state["material"] = 0
        result = core.draw(state, 10)
        self.assertFalse(result)

    def test_06_crack_once(self):
        state = core.new_game()
        core.crack(state)
        self.assertEqual(state["rate"], 90)

    def test_07_no_anneal_without_annealing(self):
        state = core.new_game()
        state["annealing"] = 0
        result = core.anneal(state, 1)
        self.assertFalse(result)

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
