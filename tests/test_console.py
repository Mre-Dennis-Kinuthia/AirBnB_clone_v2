def test_create_with_params(self):
    """Test create command with parameters"""
    cmd = 'create State name="California" code="CA" population=39538223'
    self.cli.do_create(cmd)
    out = self.stdout.getvalue().strip()
    self.assertTrue(len(out) == 36)  # length of UUID
    self.assertIn("State", storage.all())
    obj_id = "State." + out
    obj = storage.all()[obj_id]
    self.assertEqual(obj.name, "California")
    self.assertEqual(obj.code, "CA")
    self.assertEqual(obj.population, 39538223)
