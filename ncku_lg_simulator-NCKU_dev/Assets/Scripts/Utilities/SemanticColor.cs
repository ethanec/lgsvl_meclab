/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

using System;
using UnityEngine;

namespace Simulator.Utilities
{
    [Serializable]
    public class SemanticColor
    {
        [TagSelector]
        public string Tag;
        public Color Color;
    }
}
