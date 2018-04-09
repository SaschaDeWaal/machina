using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RobotMovement : MonoBehaviour {

	private const float fieldSize = 20;

	[Header("Emotion")]
	public int happiness;
	public int insicure;
	public int angry;

	[Header("Movement")]
	public float rotateSpeed = 10;
	public float moveSpeed = 5;
	public float targetLenght = 5;

	private Vector2 targetPosition = new Vector2();

	private void Start () {
		SetTarget();
	}
	
	private void Update () {
		RotateTowardsPosition();
		MoveForward();

		if (Vector2.Distance(new Vector2(transform.position.x, transform.position.z), targetPosition) < 2) {
			SetTarget();
		}
	}

	private void RotateTowardsPosition() {
		Vector3 dir = new Vector3(targetPosition.x, transform.position.y, targetPosition.y) - transform.position;

		Quaternion targetRotation = Quaternion.LookRotation(dir);
		transform.rotation = Quaternion.RotateTowards(transform.rotation, targetRotation, rotateSpeed * Time.deltaTime);
	}

	private void MoveForward() {
		transform.Translate(Vector3.forward * Time.deltaTime * moveSpeed);
	}

	private void SetTarget() {
		bool foundTarget = false;

		if (targetLenght < 1 || targetLenght > fieldSize * 0.5) {
			targetLenght = 5;
		}

		while (foundTarget == false) {
			targetPosition = new Vector2(Random.Range(fieldSize * -0.5f, fieldSize * 0.5f), Random.Range(fieldSize * -0.5f, fieldSize * 0.5f));
			float distance = Vector2.Distance(new Vector2(transform.position.x, transform.position.z), targetPosition);
			foundTarget = (distance > targetLenght * 0.8 && distance < targetLenght * 1.2f);
		}
	}
}
