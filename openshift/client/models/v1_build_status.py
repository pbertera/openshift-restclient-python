# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1BuildStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cancelled': 'bool',
        'completion_timestamp': 'datetime',
        'config': 'V1ObjectReference',
        'duration': 'int',
        'log_snippet': 'str',
        'message': 'str',
        'output': 'V1BuildStatusOutput',
        'output_docker_image_reference': 'str',
        'phase': 'str',
        'reason': 'str',
        'stages': 'list[V1StageInfo]',
        'start_timestamp': 'datetime'
    }

    attribute_map = {
        'cancelled': 'cancelled',
        'completion_timestamp': 'completionTimestamp',
        'config': 'config',
        'duration': 'duration',
        'log_snippet': 'logSnippet',
        'message': 'message',
        'output': 'output',
        'output_docker_image_reference': 'outputDockerImageReference',
        'phase': 'phase',
        'reason': 'reason',
        'stages': 'stages',
        'start_timestamp': 'startTimestamp'
    }

    def __init__(self, cancelled=None, completion_timestamp=None, config=None, duration=None, log_snippet=None, message=None, output=None, output_docker_image_reference=None, phase=None, reason=None, stages=None, start_timestamp=None):
        """
        V1BuildStatus - a model defined in Swagger
        """

        self._cancelled = None
        self._completion_timestamp = None
        self._config = None
        self._duration = None
        self._log_snippet = None
        self._message = None
        self._output = None
        self._output_docker_image_reference = None
        self._phase = None
        self._reason = None
        self._stages = None
        self._start_timestamp = None
        self.discriminator = None

        if cancelled is not None:
          self.cancelled = cancelled
        if completion_timestamp is not None:
          self.completion_timestamp = completion_timestamp
        if config is not None:
          self.config = config
        if duration is not None:
          self.duration = duration
        if log_snippet is not None:
          self.log_snippet = log_snippet
        if message is not None:
          self.message = message
        if output is not None:
          self.output = output
        if output_docker_image_reference is not None:
          self.output_docker_image_reference = output_docker_image_reference
        self.phase = phase
        if reason is not None:
          self.reason = reason
        if stages is not None:
          self.stages = stages
        if start_timestamp is not None:
          self.start_timestamp = start_timestamp

    @property
    def cancelled(self):
        """
        Gets the cancelled of this V1BuildStatus.
        cancelled describes if a cancel event was triggered for the build.

        :return: The cancelled of this V1BuildStatus.
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """
        Sets the cancelled of this V1BuildStatus.
        cancelled describes if a cancel event was triggered for the build.

        :param cancelled: The cancelled of this V1BuildStatus.
        :type: bool
        """

        self._cancelled = cancelled

    @property
    def completion_timestamp(self):
        """
        Gets the completion_timestamp of this V1BuildStatus.
        completionTimestamp is a timestamp representing the server time when this Build was finished, whether that build failed or succeeded.  It reflects the time at which the Pod running the Build terminated. It is represented in RFC3339 form and is in UTC.

        :return: The completion_timestamp of this V1BuildStatus.
        :rtype: datetime
        """
        return self._completion_timestamp

    @completion_timestamp.setter
    def completion_timestamp(self, completion_timestamp):
        """
        Sets the completion_timestamp of this V1BuildStatus.
        completionTimestamp is a timestamp representing the server time when this Build was finished, whether that build failed or succeeded.  It reflects the time at which the Pod running the Build terminated. It is represented in RFC3339 form and is in UTC.

        :param completion_timestamp: The completion_timestamp of this V1BuildStatus.
        :type: datetime
        """

        self._completion_timestamp = completion_timestamp

    @property
    def config(self):
        """
        Gets the config of this V1BuildStatus.
        config is an ObjectReference to the BuildConfig this Build is based on.

        :return: The config of this V1BuildStatus.
        :rtype: V1ObjectReference
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this V1BuildStatus.
        config is an ObjectReference to the BuildConfig this Build is based on.

        :param config: The config of this V1BuildStatus.
        :type: V1ObjectReference
        """

        self._config = config

    @property
    def duration(self):
        """
        Gets the duration of this V1BuildStatus.
        duration contains time.Duration object describing build time.

        :return: The duration of this V1BuildStatus.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this V1BuildStatus.
        duration contains time.Duration object describing build time.

        :param duration: The duration of this V1BuildStatus.
        :type: int
        """

        self._duration = duration

    @property
    def log_snippet(self):
        """
        Gets the log_snippet of this V1BuildStatus.
        logSnippet is the last few lines of the build log.  This value is only set for builds that failed.

        :return: The log_snippet of this V1BuildStatus.
        :rtype: str
        """
        return self._log_snippet

    @log_snippet.setter
    def log_snippet(self, log_snippet):
        """
        Sets the log_snippet of this V1BuildStatus.
        logSnippet is the last few lines of the build log.  This value is only set for builds that failed.

        :param log_snippet: The log_snippet of this V1BuildStatus.
        :type: str
        """

        self._log_snippet = log_snippet

    @property
    def message(self):
        """
        Gets the message of this V1BuildStatus.
        message is a human-readable message indicating details about why the build has this status.

        :return: The message of this V1BuildStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1BuildStatus.
        message is a human-readable message indicating details about why the build has this status.

        :param message: The message of this V1BuildStatus.
        :type: str
        """

        self._message = message

    @property
    def output(self):
        """
        Gets the output of this V1BuildStatus.
        output describes the Docker image the build has produced.

        :return: The output of this V1BuildStatus.
        :rtype: V1BuildStatusOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this V1BuildStatus.
        output describes the Docker image the build has produced.

        :param output: The output of this V1BuildStatus.
        :type: V1BuildStatusOutput
        """

        self._output = output

    @property
    def output_docker_image_reference(self):
        """
        Gets the output_docker_image_reference of this V1BuildStatus.
        outputDockerImageReference contains a reference to the Docker image that will be built by this build. Its value is computed from Build.Spec.Output.To, and should include the registry address, so that it can be used to push and pull the image.

        :return: The output_docker_image_reference of this V1BuildStatus.
        :rtype: str
        """
        return self._output_docker_image_reference

    @output_docker_image_reference.setter
    def output_docker_image_reference(self, output_docker_image_reference):
        """
        Sets the output_docker_image_reference of this V1BuildStatus.
        outputDockerImageReference contains a reference to the Docker image that will be built by this build. Its value is computed from Build.Spec.Output.To, and should include the registry address, so that it can be used to push and pull the image.

        :param output_docker_image_reference: The output_docker_image_reference of this V1BuildStatus.
        :type: str
        """

        self._output_docker_image_reference = output_docker_image_reference

    @property
    def phase(self):
        """
        Gets the phase of this V1BuildStatus.
        phase is the point in the build lifecycle. Possible values are \"New\", \"Pending\", \"Running\", \"Complete\", \"Failed\", \"Error\", and \"Cancelled\".

        :return: The phase of this V1BuildStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1BuildStatus.
        phase is the point in the build lifecycle. Possible values are \"New\", \"Pending\", \"Running\", \"Complete\", \"Failed\", \"Error\", and \"Cancelled\".

        :param phase: The phase of this V1BuildStatus.
        :type: str
        """
        if phase is None:
            raise ValueError("Invalid value for `phase`, must not be `None`")

        self._phase = phase

    @property
    def reason(self):
        """
        Gets the reason of this V1BuildStatus.
        reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.

        :return: The reason of this V1BuildStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1BuildStatus.
        reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.

        :param reason: The reason of this V1BuildStatus.
        :type: str
        """

        self._reason = reason

    @property
    def stages(self):
        """
        Gets the stages of this V1BuildStatus.
        stages contains details about each stage that occurs during the build including start time, duration (in milliseconds), and the steps that occured within each stage.

        :return: The stages of this V1BuildStatus.
        :rtype: list[V1StageInfo]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this V1BuildStatus.
        stages contains details about each stage that occurs during the build including start time, duration (in milliseconds), and the steps that occured within each stage.

        :param stages: The stages of this V1BuildStatus.
        :type: list[V1StageInfo]
        """

        self._stages = stages

    @property
    def start_timestamp(self):
        """
        Gets the start_timestamp of this V1BuildStatus.
        startTimestamp is a timestamp representing the server time when this Build started running in a Pod. It is represented in RFC3339 form and is in UTC.

        :return: The start_timestamp of this V1BuildStatus.
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this V1BuildStatus.
        startTimestamp is a timestamp representing the server time when this Build started running in a Pod. It is represented in RFC3339 form and is in UTC.

        :param start_timestamp: The start_timestamp of this V1BuildStatus.
        :type: datetime
        """

        self._start_timestamp = start_timestamp

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1BuildStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other