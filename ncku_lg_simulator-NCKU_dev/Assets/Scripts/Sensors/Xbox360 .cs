using System.Collections;

using System.Collections.Generic;

using UnityEngine;



public class Xbox360 : MonoBehaviour
{

    public float xAix, yAix;

    void Update()
    {

        xAix = Input.GetAxis("Horizontal");

        yAix = Input.GetAxis("Vertical");

    }

}