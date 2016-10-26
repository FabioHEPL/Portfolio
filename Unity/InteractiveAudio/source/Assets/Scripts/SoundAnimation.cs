using UnityEngine;
using System.Collections;


public class SoundAnimation : MonoBehaviour
{
    private AudioSource _audioSource = null;
    private AudioClip animatorClip = null;
     
    public float scaling = 20f;

    private float[] signalAmplitude = new float[512];

    public float tresholdAmplitude = 0.2f;

    public float animLag = 0.1f;

    Vector3 startPosition;

    private Vector3 translateVelocity = Vector3.zero;
    private Vector3 resetVelocity = Vector3.zero;
    public float smoothing = 0.1f;
    public float resetSmoothing = 0.05f;

    public bool smoothMovement = true;


	// Use this for initialization
	void Start ()
	{
        startPosition = transform.position;
        _audioSource = GetComponent<AudioSource>();
        animatorClip = _audioSource.clip;
	}
	
	// Update is called once per frame
	void Update ()
	{
        _audioSource.GetOutputData(signalAmplitude, 0);
        float amplitude = calculateAmplitude(signalAmplitude);

        if (smoothMovement)
        {
            if (amplitude < tresholdAmplitude)
            {
                StartCoroutine(animateObject(startPosition));
            }
            else
            {
                
                Vector3 newPosition = new Vector3(transform.position.x, amplitude*scaling, transform.position.z);
                StartCoroutine(animateObject(newPosition));
            }
        }
        else
        {
            if (amplitude < tresholdAmplitude)
            {
                transform.position = startPosition;
            }
            else
            {
                transform.position = new Vector3(transform.position.x, (float)System.Math.Pow(amplitude + 1, scaling), transform.position.z);
            }
        }
	}


    public IEnumerator animateObject(Vector3 newPosition)
    {
        yield return new WaitForSeconds(animLag);

        transform.position = Vector3.SmoothDamp(transform.position, newPosition, ref translateVelocity, smoothing);

    }


    public float calculateAmplitude(float[] samples)
    {
        float samplesSum = 0f;
        
        for (int i = 0; i < samples.Length; i++)
        {
            samplesSum += samples[i] * samples[i];
        }

        return (float)System.Math.Sqrt(samplesSum / samples.Length);
    }
}
