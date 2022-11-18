/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

using SimpleJSON;

namespace Simulator.Api.Commands
{
    class GetCurrentScene : ICommand
    {
        public string Name => "simulator/current_scene";

        public void Execute(JSONNode args)
        {
            var api = ApiManager.Instance;
            var scene = api.CurrentScene;
            if (string.IsNullOrEmpty(scene))
            {
                api.SendResult();
            }
            else
            {
                api.SendResult(new JSONString(scene));
            }
        }
    }
}
