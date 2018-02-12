"""
Defines enumerations of all classes
"""

from enum import Enum

class MeasurementEnum(Enum):

    @classmethod
    def get_code(cls, val):
        """
        returns the value of a given attribute in an enum collection
        :param val: attribute name in the enum
        :return: corresponding attribute value in the enum
        """
        if val == "":
            return ""
        if val == 'in' and cls.__name__ == 'UnitSymbolKind':
            val = 'inch'
        if val not in cls.__members__:
            raise ValueError("Type not defined in: " + cls.__name__)
        return cls[val].value


class AccumulationKind(MeasurementEnum):
    """
            This class provides metadata about how the measurements described are made.
            These enumerated values refer to the common present and historic methods by
            which physical measurements are made in revenue-quality metering instruments
            and are based on that terminology.

            The attributes present in AccumulationKind collection are:

                'none': Not Applicable, or implied by the unit of measure.

                'bulkQuantity': A value from a register which represents the bulk quantity of a commodity. This
                quantity is computed as the integral of the commodity usage rate. This value is
                typically used as the basis for the dial reading at the meter, and as a result,
                will roll over upon reaching a maximum dial value.
                Note 1: With the metering system, the roll-over behavior typically implies a
                roll-under behavior so that the value presented is always a positive value (e.g.
                , unsigned integer or positive decimal.) However, when communicating data
                between enterprise applications a negative value might occur in a case such as
                net metering.
                Note 2: A BulkQuantity refers primarily to the dial reading and not the
                consumption over a specific period of time.

                'continuousCumulative': The sum of the previous billing period values and the present period value.
                Note: "ContinuousCumulative" is commonly used in conjunction with "demand." The
                "ContinuousCumulative Demand" would be the cumulative sum of the previous
                billing period maximum demand values (as occurring with each demand reset)
                summed with the present period maximum demand value (which has yet to be reset.)

                'cumulative': The sum of the previous billing period values. Note: "Cumulative" is commonly
                used in conjunction with "demand." Each demand reset causes the maximum demand
                value for the present billing period (since the last demand reset) to
                accumulate as an accumulative total of all maximum demands. So instead of
                "zeroing" the demand register, a demand reset has the affect of adding the
                present maximum demand to this accumulating total.

                'deltaData': The difference between the value at the end of the prescribed interval and the
                beginning of the interval. This is used for incremental interval data.
                Note: One common application would be for load profile data, another use might
                be to report the number of events within an interval (such as the number of
                equipment energizations within the specified period of time.)

                'summation': As if a needle is swung out on the meter face to a value to indicate the
                current value. (Note: An "indicating" value is typically measured over hundreds
                of milliseconds or greater, or may imply a "pusher" mechanism to capture a
                value. Compare this to "instantaneous" which is measured over a shorter period
                of time.)indicating,
                A form of accumulation which is selective with respect to time.
                Note : "Summation" could be considered a specialization of "Bulk Quantity"
                according to the rules of inheritance where "Summation" selectively accumulates
                pulses over a timing pattern, and "BulkQuantity" accumulates pulses all of the
                time.

                'timeDelay': A form of computation which introduces a time delay characteristic to the data
                value

                'instantaneous':Typically measured over the fastest period of time allowed by the definition of
                the metric (usually milliseconds or tens of milliseconds.) (Note:
                "Instantaneous" was moved to attribute #3 in 61968-9Ed2 from attribute #1 in
                61968-9Ed1.)

                'latchingQuantity': When this description is applied to a metered value, it implies that the value
                is a time-independent cumulative quantity much a BulkQuantity, except that it
                latches upon the maximum value upon reaching that value. Any additional
                accumulation (positive or negative) is discarded until a reset occurs.
                Note: A LatchingQuantity may also occur in the downward direction  upon
                reaching a minimum value. The terms "maximum" or "minimum" will usually be
                included as an attribute when this type of accumulation behaviour is present.
                When this description is applied to an encoded value (UOM= "Code"), it implies
                that the value has one or more bits which are latching. The condition that
                caused the bit to be set may have long since evaporated.
                In either case, the timestamp that accompanies the value may not coincide with
                the moment the value was initially set.
                In both cases a system will need to perform an operation to clear the latched
                value.

                'boundedQuantity': A time-independent cumulative quantity such as BulkQuantity or a
                LatchingQuantity, except that the accumulation stops at the maximum or minimum
                values. When the maximum is reached, any additional positive accumulation is
                discarded, but negative accumulation may be accepted (thus lowering the counter.
                ) Likewise, when the negative bound is reached, any additional negative
                accumulation is discarded, but positive accumulation is accepted (thus
                increasing the counter.)
        """
    none = 1
    bulkQuantity = 2
    continuousCumulative = 3
    cumulative = 4
    deltaData = 6
    summation = 9
    timeDelay = 10
    instantaneous = 12
    latchingQuantity = 13
    boundedQuantity = 14

class DataQualifierKind(MeasurementEnum):

    """
            This class qualifies the measurement as to what it represents -- for example a
            minimum or maximum value or a nominal or nameplate value.

            The attributes present in DataQualifierKind collection are:

            high: Typically used to identify the high volume flow port of a compound water meter.
            low:  Typically used to identify the low volume flow port of a compound water meter.
            none:  Not Applicable.
            average:  The value represents an average.
            excess:  The value represents an amount over which a threshold was exceeded.
            highThreshold:  The value represents a programmed threshold.
            lowThreshold:  The value represents a programmed threshold.
            maximum:  The highest value observed.
            minimum:  The smallest value observed.
            nominal:  The value represents nominal or nameplate values.
            normal:  The value represents typical operating values.
            secondMaximum:  The second highest value observed.
            secondMinimum:  The second smallest value observed.
            thirdMaximum:  The third highest value observed.
            fourthMaximum:  The fourth highest value observed.
            fifthMaximum:  The fifth highest value observed
            sum:  The accumulated sum
        """
    average = 2
    excess = 4
    fifthMaximum = 25
    fourthMaximum = 24
    high = 27
    highThreshold = 5
    low = 28
    lowThreshold = 7
    maximum = 8
    minimum = 9
    nominal = 11
    none = 0
    normal = 12
    secondMaximum = 16
    secondMinimum = 17
    sum = 26
    thirdMaximum = 23

class QualityOfReading(MeasurementEnum):
    """
        contains List of codes indicating the quality of the reading.

        The attributes present in QualityOfReading collection are:

        estimated: The quality is estimated.
        forecast: This is forecast data.
        mixed: There is a mixture of data quality.
        raw: This is raw data.
        validated: This data has been validated.
        normalizedForWeather: This data has been normalized for weather.
        other: There is no defined quality for this data
    """
    estimated = 0
    forecast = 1
    mixed = 2
    raw = 3
    validated = 4
    normalizedForWeather = 5
    other = 6

class UnitSymbolKind(MeasurementEnum):

    """
        This class identifies the units of measure based on the NIST Special Publication 811
        2008 edition -- Guide for the Use of the International System of Units (SI).
        Note that these reference document supports SI units as well as common units of
        measurements in practice including CGS units.

          Only VA, W, var, VAh, Wh, varh, Btu, J, therm, BtuPerh, g, gPerM3, gPerS, m,
        mPerS, WPerM2, rad, sb, pa, and degK are normative for the FSGIM standard.  The
        enumerated values of VA, W, var, VAh, Wh, and varh were changed from their
        original NAESB values of vA, w, vAr, vAH, wH, and vArH to make them consistent
        with the standard SI abbreviations for these units.  The enumerated values of
        Btu and BtuPerh were changed from their original NAESB values of btu and
        btuPerH to make them consistent with the standard abbreviations for British
        thermal units and hours.

          Note:  The abbreviation MBtu is often used to represent thousands of Btu's
        (where M represents the Roman numeral for 1000).  The FSGIM <i>always </i>uses
        the SI prefixes listed in the SiScaleCodeType enumeration and not the prefixes
        based on Roman numerals.  This means that 1000 Btu's would be represented in
        the FSGIM as EnergyThermalQuantity.quantity = 1, EnergyThermalType.itemUnits =
        Btu, and EnergyThermalType.siScaleCode = k, <i>not </i>EnergyThermalType.
        siScaleCode = M.

        The attributes present in UnitSymbolKind collection are:
            m: Length,meter
            g: Mass,gram
            a: Current,ampere
            degK: Temperature,Kelvin (Note: the unit "degrees" is implied)
            mol: Amount of substance,mole
            cd: Luminous intensity,candela
            s: Time,second
            rad: Plane angle,Radian (m/m)
            sr: Solid angle,Steradian (m2/m2)
            gy: Absorbed dose,Gray (J/kg)
            bq: Radioactivity,Becquerel (1/s)
            degC: Relative temperature,degrees Celsius
            sv: Dose equivalent,Sievert (J/kg)
            f: Electric capacitance,Farad (C/V)
            c: Electric charge,Coulomb (Amp second)
            h: Electric inductance,Henry (Wb/A)
            v: Electric potential,Volt (W/A)
            ohm: Electric resistance,Ohm (V/A)
            J: Energy joule,(N�m = C�V = W�s)
            n: Force newton,(kg m/s�)
            hz: Frequency,Cycles per second or (1/s)
            lx: Illuminance lux,(lm/m2)
            lm: Luminous flux,lumen (cd sr)
            wb: Magnetic flux,Weber (V s)
            t: Magnetic flux density,Tesla (Wb/m2)
            W: Real power,Watt. By definition, one Watt equals one Joule per second. Electrical power may have real and reactive components. The real portion of electrical power (I�R) or VIcos?, is expressed in Watts. (See also apparent power and reactive power.)
            pa: Pressure,Pascal (N/m2) (Note: the absolute or relative measurement of pressure is implied with this entry. See below for more explicit forms.)
            siemens: Electric Conductance,Siemens (A / V = 1 / O)
            paA: Pressure,Pascal, absolute pressure
            paG: Pressure,Pascal, gauge pressure
            kat: Catalytic activity,katal = mol / s
            revPerS: Rotational speed,rotations per second (Note: compare to cycles per second, Hz)
            m2: Area,square meter
            m3: Volume,cubic meter
            mPerS: Velocity,meter per second (m/s)
            mPerS2: Acceleration,meter per second squared
            m3PerS: Volumetric flow rate,cubic meters per second
            mPerM3: Fuel efficiency,meter / cubic meter
            gM: Moment of mass,kilogram meter (kg�m) (first moment of mass) (Note: users must supply the "k" prefix to obtain "kg m".)
            gPerM3: Density,gram/cubic meter (Note: users must supply the prefix multiplier "k" to form kg/ m�)
            m2PerS: Viscosity,meter squared / second
            wPerMK: Thermal conductivity,Watt/meter Kelvin
            jPerK: Heat capacity,Joule/Kelvin
            radPerS: Angular velocity,radians per second
            VA: Apparent power,Volt Ampere (See also real power and reactive power.)
            var: Reactive power,Volt Ampere reactive. The "reactive" or "imaginary" component of electrical power (VISin?). (See also real power and apparent power).
            vS: Volt seconds,Volt seconds (Ws/A)
            v2: Volts squared,Volt squared (W2/A2)
            aS: Amp seconds,Amp seconds
            a2: Amps squared,Amp squared
            a2S: Amps squared time,square Amp second
            VAh: Apparent energy,Volt Ampere hours
            Wh: Real energy,Watt hours
            varh: Reactive energy,Volt Ampere reactive hours
            vPerHz: Magnetic flux,Volt per Hertz
            hzPerS: Rate of change of frequency,Hertz per second
            gM2: Moment of mass,kg m2 (Second moment of mass, commonly called the moment of inertia) (Note: users must supply the "k" prefix to obtain "kg m2".)
            wPerS: Ramp rate,Watt per second
            lPerS: Volumetric flow rate,liters per second
            q: Quantity power,Q
            qh: Quantity energy,Qh
            ohmM: resistivity,Ohm meter, ? (rho)
            aPerM: A/m,magnetic field strength, Ampere per meter
            v2H: volt-squared hour,Volt-squared-hours
            a2H: ampere-squared hour,Ampere-squared hour
            aH: Ampere-hours,Ampere-hours
            wHPerM3: Wh/m3,energy per volume
            timeStamp: Timestamp,time and date per ISO 8601 format
            wHPerRev: Kh-Wh,active energy metering constant
            vArHPerRev: Kh-VArh,reactive energy metering constant
            vAHPerRev: Kh-Vah,apparent energy metering constant
            m3PerH: Volumetric flow rate,cubic meter per hour
            m3CompensatedPerH: Volumetric flow rate,compensated cubic meter per hour
            m3UncompensatedPerH: Volumetric flow rate,uncompensated cubic meter per hour
            lPerH: Volumetric flow rate,liter per hour
            lUncompensatedPerH: Volumetric flow rate,liter (uncompensated) per hour
            lCompensatedPerH: Volumetric flow rate,liter (compensated) per hour
            q45: Quantity power,Q measured at 45�
            q60: Quantity power,Q measured at 60�
            q45H: Quantity energy,Qh measured at 45�
            q60H: Quantity energy,Qh measured at 60�
            jPerKg: Specific energy,Joule / kg
            m3Uncompensated: Volume,cubic meter, with the value uncompensated for weather effects.
            m3Compensated: Volume,cubic meter, with the value compensated for weather effects.
            m1: Wavenumber,reciprocal meter, (1/m)
            m3PerKg: Specific volume,cubic meter per kilogram, v
            paS: Dynamic viscosity,Pascal second
            nM: Moment of force,Newton meter
            nPerM: Surface tension,Newton per meter
            radPerS2: Angular acceleration,radian per second squared
            wPerM2: Heat flux density, irradiance,Watt per square meter
            jPerKgK: Specific heat capacity, specific entropy,Joule per kilogram kelvin
            jPerM3: energy density,Joule per cubic meter
            vPerM: electric field strength,Volt per meter
            cPerM3: electric charge density,Coulomb per cubic meter
            cPerM2: surface charge density,Coulomb per square meter
            fPerM: permittivity,Farad per meter
            hPerM: permeability,Henry per meter
            jPerMol: molar energy,Joule per mole
            jPerMolK: molar entropy, molar heat capacity,Joule per mole kelvin
            cPerKg: exposure (x rays),Coulomb per kilogram
            gyPerS: absorbed dose rate,Gray per second
            wPerSr: radiant intensity,Watt per steradian
            wPerM2Sr: radiance,Watt per square meter steradian
            katPerM3: catalytic activity concentration,katal per cubic meter
            min: Time,minute = 60 s
            hr: Time,hour = 60 min = 3600 s
            d: Time,day = 24 h = 86400 s
            deg: Plane angle,degree
            angleMin: Plane angle,minute
            angleSec: Plane angle,second
            ha: Area,hectare
            l: Volume,liter= dm3 = m3/1000.
            tonne: mass,"tonne" or "metric ton" (1000 kg = 1 Mg)
            none: N/A,none (not applicable)
            cosTheta: Power factor,dimensionless
            bel: Logrithmic ratio,Bel, Note: users must combine this unit with the multiplier prefix "d" to form decibels (dB)
            status: State,status, where:"1" = "true", "live", "on", "high", "set";"0" = "false", "dead", "off", "low", "cleared"Note: A Boolean value is preferred but other values may be supported
            count: Amount of substance,Counter value
            bm: Logrithmic ratio of signal strength,Bel-mW, normalized to 1mW. Note: to form "dBm" combine "Bm" with multiplier "d".
            code: Application Value,Encoded value
            meCode: EndDeviceEvent,Value to be interpreted as a EndDeviceEventCode
            lPerL: Concentration,The ratio of the volume of a solute divided by the volume of the solution. (Note: Users may need use a prefix such a '�' to express a quantitye such as '�L/L')
            gPerG: Concentration,The ratio of the mass of a solute divided by the mass of the solution. (Note: Users may need use a prefix such a '�' to express a quantity such as '�g/g')
            molPerM3: Concentration,The amount of substance concentration, (c), the amount of solvent in moles divided by the volume of solution in m�.
            molPerMol: Concentration,Molar fraction, the ratio of the molar amount of a solute divided by the molar amount of the solution.
            molPerKg: Concentration,Molality, the amount of solute in moles and the amount of solvent in kilograms.
            mPerM: Length,Ratio of length
            sPerS: Time,Ratio of time (Note: Users may need to supply a prefix such as '�' to show rates such as '�s/s')
            hzPerHz: Frequency,Rate of frequency change (Note: Users may need to supply a prefix such as 'm' to show rates such as 'mHz/Hz')
            vPerV: Voltage,Ratio of voltages (Note: Users may need to supply a prefix such as 'm' to show rates such as 'mV/V')
            aPerA: Current,Ratio of Amperages (Note: Users may need to supply a prefix such as 'm' to show rates such as 'mA/A')
            wPerVA: Power factor,PF
            rev: Amount of rotation,Revolutions
            wPerW: Signal Strength,Ratio of power (Note: Users may need to supply a prefix such as 'm' to show rates such as 'mW/W')
            refractiveIndexN: Refractive Index,n
            relativePermeabilityMur: Relative Permeability,�r
            np: Logarithmic ratio,neper
            eV: energy,electronvolt (1 eV = 1.602 176 x 10-19J)
            da: mass,dalton (1 Da = 1.660 538 x 10-27kg)
            u: mass,unified atomic mass unit (1u = 1 Da)
            ua: length,astronomical unit (1ua = 1.495 978 x1011m)
            c0: speed,natural unit of speed (speed of light in a vacuum) 299 792 458 m/s
            nuH: action,natural unit of action (reduced planck constant) 1.054 571 X 10-34J s
            nuMe: mass,natural unit of mass (electron mass) 9.109 382 x 10-31 kg
            nuHPerNuMeC02: time,natural unit of time
            auE: charge,atomic units of charge (elementary charge) 1.602 176 x 10-19 C
            auMe: mass,atomic units of mass (electron mass) 9.109 382 x 10-31 kg
            auH: action,atomic unit of action (reduced planck constant) 1.054 571 X 10-34J s
            auA0: length,atomic unit of length, bohr ( Bohr radius) 0.529 177 x 10-10 m
            auEh: energy,atomic unit of energy, hartree 4.359 744
            auHPerAuEh: time,atomic unit of time
            char: Number of characters,characters
            charPerSec: Data rate,characters per second
            money: Monetary unit,Generic money (Note: Specific monetary units are identified the currency class).
            ft3: Volume,cubic foot
            ft3Compensated: Volume,cubic foot compensated for weather
            ft3Uncompensated: Volume,cubic foot uncompensated for weather
            ft3PerH: Volumetric flow rate,cubic foot per hour
            ft3CompensatedPerH: Volumetric flow rate,compensated cubic feet per hour
            ft3UncompensatedPerH: Volumetric flow rate,uncompensated cubic feet per hour
            uSGal: Volume,US gallon (1 gal = 231 in3 = 128 fl oz.)
            uSGalPerH: Volumetric flow rate,US gallon per hour
            impGal: Volume,Imperial gallon
            impGalPerH: Volumetric flow rate,Imperial gallon per hour
            Btu: Energy, British Thermal Unit ref: 59 degrees F
            BtuPerH: Power,BTU per hour
            psiA: Pressure,Pound per square inch, absolute
            psiG: Pressure,Pound per square inch, gauge
            lUncompensated: Volume,Liter, with the value uncompensated for weather effects.
            lCompensated: Volume,Liter, with the value compensated for weather effects.
            therm: Energy,Therm
            bar: Pressure,bar (1 bar = 100 kPa)
            mmHg: Pressure,millimeter of mercury (1 mmHg � 133.3 Pa)
            angstrom: Length,�ngstr�m (1� = 10-10m)
            nmi: Length,nautical mile (1 M = 1852 m)
            barn: Area,barn (1 b = 100 fm2 = 10-28 m2)
            kn: Speed,knot (1 kn = 1852/3600) m/s
            ci: Activity,curie (1 Ci = 3.7 x 1010Bq)
            r: exposure,roentgen (1 R = 2.58 x 10-4 C/kg)
            doseRad: absorbed dose,rad (1 rd = 1 cGy)
            rem: dose equivalent,rem (1 rem = 10-2 Sv)
            in: length,inch
            ft: length,foot (1 ft = 12 in)
            rod: length,rod (1 rod = 16.5 ft)
            fur: length,furlong (1 fur = 660 ft)
            mi: length,mile (1 statute mile = 8 fur = 80 chains = 320 rods = 5280 feet)
            ft2: area,square foot (1 ft2 = 144 in2)
            yd2: area,square yard (1 yd2 = 9 ft2)
            rod2: area,square rod (1 rod2 = 272.25 ft2)
            acre: area,acre (1 acre = 160 rd2 = 43 560 ft2)
            mi2: area,square mile (1 mi2 = 640 acres)
            sectionOfLand: area,section of land (1 mi2 = 1 section of land)
            township: area,township (1 township = 6 miles square)
            yd3: Volume,cubic yard (1 yd3 = 27 ft3)
            li: length,link (1 li = 0.66 ft)
            ch: length,chain (1 ch = 100 links = 4 rods = 66 ft)
            uSLiqPt: Volume,US liquid pint (1 pt = 28.875 in3 = 128 fl dr)
            uSLiqQt: Volume,US liquid quart (1 qt = 2 pt)
            flDrAp: Volume,Apothecaries fluid dram
            flOzAp: Volume,Apothecaries fluid ounce (1 fl oz ap = 8 fl dr ap)
            usDryPt: Volume,US dry pint (1 pt = 67.2 in3)
            usDryQt: Volume,US dry quart (1 qt = 2 pints)
            usPk: Volume,US peck (1 pk = 8 qt)
            usBu: Volume,US bushel (1 bu = 4 pk)
            gr: Mass,grain (1 grain = 1/7000 avdp lb) Note: The "grain" is the same in the avoirdupois, troy, and apothecaries units of mass.
            avdpDr: Mass,Avoirdupois dram (1 Avdp dr = 27-11/32 gr) Note: The abbreviation "dr" may be used if there is no chance of confusing the avoirdupois dram with the troy or apothecaries dram.
            avdpOz: Mass,Avoirdupois ounce (1 Avdp oz = 16 Avdp dr) Note: The abbreviation "oz" may be used if there is no chance of confusing the avoirdupois ounce with the troy or apothecaries ounce.
            avdpLb: Mass,Avoirdupois pound (1 lb = 16 oz) Note: Although the term "pound" is commonly used in many countries simply as "pound (lb)", the historical term "avoirdupois" is added to provide context and distinguish it in this setting from the troy and apothecaries systems of measure which use the same names. The abbreviation "lb" may be used instead of "avdp lb" if no confusion is possible with the pound named in these other systems.
            shortCwt: Mass,Avoirdupois hundredweight (1 cwt = 100 lbs)
            shortTon: Mass,Avoirdupois ton (1 short ton = 2000 lbs)
            longCwt: Mass,Avoirdupois gross or long hundredweight (1 long cwt = 112 lbs)
            longTon: Mass,Avoirdupois gross or long ton (1 long ton = 20 long cwt)
            dwt: Mass,Troy pennyweight (1 dwt = 24 grains)
            ozT: Mass,Troy ounce (1 oz t = 20 dwt)
            lbT: Mass,Troy pound (1 lb t = 12 oz t)
            sAp: Mass,Apothecaries scruple (1 s ap = 20 grains)
            drAp: Mass,Apothecaries dram (1 dr ap = 3 s ap)
            ozAp: Mass,Apothecaries ounce (1 oz ap = 8 dr ap)
            lbAp: Mass,Apothecaries pound (1 lp ap = 12 oz ap)
            mpgImp: Fuel economy,mile per imperial gallon
            mpgUS: Fuel economy,mile per US gallon
            mPGeUS: Fuel economy,mile per US gallon equivalent
            lPer100km: Fuel economy,liter per 100 km
            wHPerMi: Fuel economy,watt-hour per mile (Note: users must supply the "k" prefix to create "kWh/mi")
            wHPer100Mi: Fuel economy,watt-hour per 100 mile (Note: users must supply the "k" prefix to create "kWh/(100 mi)")
            degF: Temperature,degrees Fahrenheit
            erg: Energy,erg (1 erg = 10-7 J)
            dyn: Force,dyne (1 dyn = 10-5 N)
            p: Dynamic viscosity,poise (1 P = 0.1 Pa s)
            st: Kinematic viscosity,stokes (1 St = 1 cm2/s)
            sb: Luminance,stilb (1 sb = 104 cd/m2)
            ph: Illuminance,phot (1 ph = 104 lx)
            gal: Acceleration,gal (1 Gal = 10-2 m s-2) Note: This "Gal" is an abbreviation for "Galileo" not "gallon"
            mx: Magnetic flux,Maxwell (1 Mx = 10-8 Wb)
            gauss: Magnetic flux density,Gauss (1 G = 10-4 T)
            oe: Magnetic field,�rsted (1 Oe = (103/4p) A/m)
            gPerS: Mass flow rate, g/s
    """

    Btu = 0
    BtuPerH = 1
    J = 2
    VA = 3
    VAh = 4
    W = 5
    Wh = 6
    a = 7
    a2 = 8
    a2H = 9
    a2S = 10
    aH = 11
    aPerA = 12
    aPerM = 13
    aS = 14
    acre = 15
    angleMin = 16
    angleSec = 17
    angstrom = 18
    auA0 = 19
    auE = 20
    auEh = 21
    auH = 22
    auHPerAuEh = 23
    auMe = 24
    avdpDr = 25
    avdpLb = 26
    avdpOz = 27
    bar = 28
    barn = 29
    bel = 30
    bm = 31
    bq = 32
    c = 33
    c0 = 34
    cPerKg = 35
    cPerM2 = 36
    cPerM3 = 37
    cd = 38
    ch = 39
    char = 40
    charPerSec = 41
    ci = 42
    code = 43
    cosTheta = 44
    count = 45
    d = 46
    da = 47
    deg = 48
    degC = 49
    degF = 50
    degK = 51
    doseRad = 52
    drAp = 53
    dwt = 54
    dyn = 55
    eV = 56
    erg = 57
    f = 58
    fPerM = 59
    flDrAp = 60
    flOzAp = 61
    ft = 62
    ft2 = 63
    ft3 = 64
    ft3Compensated = 65
    ft3CompensatedPerH = 66
    ft3PerH = 67
    ft3Uncompensated = 68
    ft3UncompensatedPerH = 69
    fur = 70
    g = 71
    gM = 72
    gM2 = 73
    gPerG = 74
    gPerM3 = 75
    gPerS = 76
    gal = 77
    gauss = 78
    gr = 79
    gy = 80
    gyPerS = 81
    h = 82
    hPerM = 83
    ha = 84
    hr = 85
    hz = 86
    hzPerHz = 87
    hzPerS = 88
    impGal = 89
    impGalPerH = 90
    inch = 91
    jPerK = 92
    jPerKg = 93
    jPerKgK = 94
    jPerM3 = 95
    jPerMol = 96
    jPerMolK = 97
    kat = 98
    katPerM3 = 99
    kn = 100
    l = 101
    lCompensated = 102
    lCompensatedPerH = 103
    lPer100km = 104
    lPerH = 105
    lPerL = 106
    lPerS = 107
    lUncompensated = 108
    lUncompensatedPerH = 109
    lbAp = 110
    lbT = 111
    li = 112
    lm = 113
    longCwt = 114
    longTon = 115
    lx = 116
    m = 117
    m1 = 118
    m2 = 119
    m2PerS = 120
    m3 = 121
    m3Compensated = 122
    m3CompensatedPerH = 123
    m3PerH = 124
    m3PerKg = 125
    m3PerS = 126
    m3Uncompensated = 127
    m3UncompensatedPerH = 128
    mPGeUS = 129
    mPerM = 130
    mPerM3 = 131
    mPerS = 132
    mPerS2 = 133
    meCode = 134
    mi = 135
    mi2 = 136
    min = 137
    mmHg = 138
    mol = 139
    molPerKg = 140
    molPerM3 = 141
    molPerMol = 142
    money = 143
    mpgImp = 144
    mpgUS = 145
    mx = 146
    n = 147
    nM = 148
    nPerM = 149
    nmi = 150
    none = 151
    np = 152
    nuH = 153
    nuHPerNuMeC02 = 154
    nuMe = 155
    oe = 156
    ohm = 157
    ohmM = 158
    ozAp = 159
    ozT = 160
    p = 161
    pa = 162
    paA = 163
    paG = 164
    paS = 165
    ph = 166
    psiA = 167
    psiG = 168
    q = 169
    q45 = 170
    q45H = 171
    q60 = 172
    q60H = 173
    qh = 174
    r = 175
    rad = 176
    radPerS = 177
    radPerS2 = 178
    refractiveIndexN = 179
    relativePermeabilityMur = 180
    rem = 181
    rev = 182
    revPerS = 183
    rod = 184
    rod2 = 185
    s = 186
    sAp = 187
    sPerS = 188
    sb = 189
    sectionOfLand = 190
    shortCwt = 191
    shortTon = 192
    siemens = 193
    sr = 194
    st = 195
    status = 196
    sv = 197
    t = 198
    therm = 199
    timeStamp = 200
    tonne = 201
    township = 202
    u = 203
    uSGal = 204
    uSGalPerH = 205
    uSLiqPt = 206
    uSLiqQt = 207
    ua = 208
    usBu = 209
    usDryPt = 210
    usDryQt = 211
    usPk = 212
    v = 213
    v2 = 214
    v2H = 215
    vAHPerRev = 216
    vArHPerRev = 217
    vPerHz = 218
    vPerM = 219
    vPerV = 220
    vS = 221
    var = 222
    varh = 223
    wHPer100Mi = 224
    wHPerM3 = 225
    wHPerMi = 226
    wHPerRev = 227
    wPerM2 = 228
    wPerM2Sr = 229
    wPerMK = 230
    wPerS = 231
    wPerSr = 232
    wPerVA = 233
    wPerW = 234
    wb = 235
    yd2 = 236
    yd3 = 237