#!/usr/bin/env python3
import os

import aws_cdk as cdk

from speed_comparison.speed_comparison_stack import SpeedComparisonStack


app = cdk.App()
SpeedComparisonStack(app, "SpeedComparisonStack")

app.synth()
