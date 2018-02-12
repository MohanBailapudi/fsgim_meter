"""
Defines enumerations of all classes
"""

from enum import Enum

class MeasurementEnum(Enum):

    @classmethod
    def get_code(cls,val):
        if val == "":
            return val
        elif any(val == item.value for item in cls) is True:
            return cls[val]


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


