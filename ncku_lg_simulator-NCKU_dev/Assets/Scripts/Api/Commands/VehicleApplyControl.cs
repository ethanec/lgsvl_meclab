/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

using SimpleJSON;
using UnityEngine;

namespace Simulator.Api.Commands
{
    class VehicleApplyControl : ICommand
    {
        public string Name => "vehicle/apply_control";

        public void Execute(JSONNode args)
        {
            var uid = args["uid"].Value;
            var api = ApiManager.Instance;

            if (api.Agents.TryGetValue(uid, out GameObject obj))
            {
                var sticky = args["sticky"].AsBool;
                var control = args["control"];

                var vc = obj.GetComponent<VehicleController>();
                var va = obj.GetComponent<VehicleActions>();
                var vd = obj.GetComponent<VehicleDynamics>();

                var steering = control["steering"].AsFloat;
                var throttle = control["throttle"].AsFloat;
                var braking = control["braking"].AsFloat;

                vc.ApplyControl(sticky, steering, throttle - braking);

                var reverse = control["reverse"].AsBool;

                if (reverse)
                    vd.ShiftReverse();
                else
                    vd.ShiftFirstGear();

                var handbrake = args["control"]["handbrake"].AsBool;
                vd.HandBrake = handbrake;

                if (args["control"]["headlights"] != null)
                {
                    int headlights = args["control"]["headlights"].AsInt;
                    va.CurrentHeadLightState = (VehicleActions.HeadLightState)headlights;
                }

                if (args["control"]["windshield_wipers"] != null)
                {
                    int state = args["control"]["windshield_wipers"].AsInt;
                    va.CurrentWiperState = (VehicleActions.WiperState)state;
                }

                if (args["control"]["turn_signal_Left"] != null)
                {
                    bool on = args["control"]["turn_signal_Left"].AsBool;
                    va.LeftTurnSignal = on;
                }

                if (args["control"]["turn_signal_right"] != null)
                {
                    bool on = args["control"]["turn_signal_right"].AsBool;
                    va.RightTurnSignal = on;
                }

                api.SendResult();
            }
            else
            {
                api.SendError($"Agent '{uid}' not found");
            }
        }
    }
}
