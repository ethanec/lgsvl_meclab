using UnityEngine;
using System.Collections;
public class MotorOvertake : MonoBehaviour
{
    private GameObject[] Agent;
    private BoxCollider OvertakeCollider;
    private GameObject OvertakeDetect;
    private void Start()
    {
        //Produce Collider on all Agent 
        Agent = GameObject.FindGameObjectsWithTag("Player");
        if (Agent == null)
        {
            Debug.Log("OvertakeCollider produce error");
        }
        else
        {   
            foreach (GameObject vehicle in Agent)
            {
                OvertakeDetect = new GameObject("OvertakeDetect");
                OvertakeDetect.transform.SetParent(transform,true);
                OvertakeCollider = OvertakeDetect.AddComponent<BoxCollider>();
                OvertakeCollider.center = new Vector3(transform.position.x ,  transform.position.y + 0.1f , transform.position.z - 8.0f);
                OvertakeCollider.size = new Vector3(12.0f , 0.0f , 0.0f);
                OvertakeCollider.isTrigger = true;
            }
        }
    }
}