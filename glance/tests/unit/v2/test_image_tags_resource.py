# Copyright 2012 OpenStack, LLC
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json

import webob

import glance.api.v2.image_tags
import glance.tests.unit.utils as unit_test_utils
import glance.tests.utils as test_utils


class TestImageTagsController(test_utils.BaseTestCase):

    def setUp(self):
        super(TestImageTagsController, self).setUp()
        self.db = unit_test_utils.FakeDB()
        self.controller = glance.api.v2.image_tags.Controller(self.db)

    def test_create_tag(self):
        request = unit_test_utils.get_fake_request()
        self.controller.update(request, unit_test_utils.UUID1, 'dink')

    def test_delete_tag(self):
        request = unit_test_utils.get_fake_request()
        self.controller.delete(request, unit_test_utils.UUID1, 'ping')

    def test_delete_tag_not_found(self):
        request = unit_test_utils.get_fake_request()
        self.assertRaises(webob.exc.HTTPNotFound, self.controller.delete,
                          request, unit_test_utils.UUID1, 'what')


class TestImagesSerializer(test_utils.BaseTestCase):

    def setUp(self):
        super(TestImagesSerializer, self).setUp()
        self.serializer = glance.api.v2.image_tags.ResponseSerializer()

    def test_create_tag(self):
        response = webob.Response()
        self.serializer.update(response, None)
        self.assertEqual(204, response.status_int)

    def test_delete_tag(self):
        response = webob.Response()
        self.serializer.delete(response, None)
        self.assertEqual(204, response.status_int)
