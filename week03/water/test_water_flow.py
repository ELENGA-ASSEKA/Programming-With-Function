#Call the functions(pytest, approx) to permit the function of the programm.
from pytest import approx
import pytest

#Let call the first def for test_water_culomn_height
def test_water_column_height():
    assert water_column_height(00, 00)==approx(00, abs=0.001)
    assert water_column_height(00, 10.0)==approx(7.5, abs=0.001)
    assert water_column_height(25.0, 00)==approx(25.0, abs=0.001)
    assert water_column_height(48.3, 12.8)==approx(57.9, abs=0.001)


#Let call the seconde def for test_pressure_gain_from_water_height
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0, 0.000)==approx(0.001, abs=0.001)
    assert pressure_gain_from_water_height(30.2, 295.628)==approx(0.001, abs=0.001)
    assert pressure_gain_from_water_height(50.0, 489.450)==approx(0.001, abs=0.001)

#Let call the third def for test_pressure_loss_from_pipe
def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75, 0.000)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75, 0.000)==approx(0.001, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018,	0.00, 0.000)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018,	1.75, -113.008)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018,	1.65,-100.462)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65, -61.576)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65, -110.884)==approx(0.001, abs=0.001)

#Let call the forth def for test_pressure_loss_from_fittings
def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3,	0.000)==approx(0.001, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0,	0.000)==approx(0.001, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2,	-0.109)==approx(0.001, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2,	-0.122)==approx(0.001, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5, -0.306)==approx(0.001, abs=0.001)

#Let call the fith def for test_reynolds_number
def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00,	0)==approx(1, abs=0.001)
    assert reynolds_number(0.048692, 1.65,	80069)==approx(1, abs=0.001) 
    assert reynolds_number(0.048692, 1.75,	84922)==approx(1, abs=0.001)
    assert reynolds_number(0.286870, 1.65,	471729)==approx(1, abs=0.001) 
    assert reynolds_number(0.286870, 1.75,	500318)==approx(1, abs=0.001)  

#Let call the sexth def for test_pressure_loss_from_pipe_reduction
def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00,	1, 0.048692, 0.000)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65,	471729,	0.048692, -163.744)==approx(0.001, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75,	500318,	0.048692, -184.182)==approx(0.001, abs=0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])