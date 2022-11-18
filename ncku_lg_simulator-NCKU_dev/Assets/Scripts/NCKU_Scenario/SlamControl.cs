using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SlamControl : MonoBehaviour {
public float m_speed = 5f;
public Camera DriverCamera;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
	 float horizontal = Input.GetAxis("Horizontal"); 
     float vertical = Input.GetAxis("Vertical"); 

     //float updown = Input.GetAxis("Updown"); 
     
     //float pitch = Input.GetAxis("Pitch"); 
     //float yaw = Input.GetAxis("Yaw"); 

     //Move
     transform.Translate(Vector3.forward * vertical * m_speed * Time.deltaTime);
     transform.Translate(Vector3.right * horizontal * m_speed * Time.deltaTime);
     //transform.Translate(Vector3.up * updown * m_speed * Time.deltaTime);

     //transform.transform.Rotate(0,1 * pitch,0);
     //transform.transform.Rotate(1 * yaw,0,0);
	}
}
